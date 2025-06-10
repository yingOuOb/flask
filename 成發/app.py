from flask import Flask, render_template , request , jsonify , json, abort,session,redirect
from flask_socketio import SocketIO, emit
from config import Config
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object(Config)  # 將配置載入 Flask 應用
mongo=PyMongo(app)  # 初始化 PyMongo，連接到 MongoDB
socketio = SocketIO (app)  # 將 SocketIO 實例綁定到 Flask 應用

@app.route("/")
def initialization():
    return render_template("home_page.html")

def login_req(func):
    def wrapper(*args, **kwargs):
        if not session.get('username'):
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper

@app.route("/register", methods=['GET', 'POST'])
def register():
    error = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        existing_userame = mongo.db.users.find_one({"username": username})
        if existing_userame:
            error += "Username already exists. Please choose a different username."
        if username and password:
            user={username: username, password: password}
            mongo.db.users.insert_one(user)
            session['username'] = username
            return redirect('/eat_lunch')
    return render_template("register.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    error=""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        existing_user = mongo.db.users.find_one({"username": username, "password": password})
        if not existing_user or existing_user['password'] != password:
            error += "Invalid username or password. Please try again."
        if username and password:
            session['status'] = "login"
            session['username'] = username  # 登入成功，設置 session
            return redirect('/')
        else:
            return render_template("login.html", error=error)
    return render_template("login.html")

@app.route("/logout")
def logout():
    if session['status'] == "login":
        session['status'] = "logout"
        session.pop('username', None)
        return redirect('/')
    else:
        return "你並未登入"

@app.route("/hello")
def hello():
    return " ha ha , there is nothing here, just a test page"

@app.route("/eat_lunch")
@login_req
def eat_lunch():
    return render_template("eat_lunch.html")

@app.route("/DONT_eat_lunch")
def dont_eat_lunch():
    return render_template("DONT_eat_lunch.html")

@socketio.on('request_restore_data')
def handle_restore_request():
    with open('lunch.json', 'r', encoding='utf-8') as f:
        restore_request_data = json.load(f)
        print(restore_request_data)
    socketio.emit('to_front_restore_request_message', restore_request_data)



@socketio.on('to_back_message')  
def handle_message(msg_rows):
    # print(f'Received message: {msg}')   # cmd print
    print('Received message8888888888888888888888888888888888888888888888888888888888888: ',msg_rows)   # cmd print
    emit('to_front_message', msg_rows, broadcast=True)  # 把點餐資料廣播給所有連線的客戶端
    # 嘗試讀取 lunch.json，如果檔案不存在或內容錯誤，則用空 list
   
    try:
        with open('lunch.json', 'r', encoding='utf-8') as f:
            new_eat_lunch_request = {}
            request_data = json.load(f)  # 原本的資料是一個 list
            print("open lunch.json success")
            # print(type(msg_rows))
            # print(msg_rows[0][1])
            
            new_eat_lunch_request["salesperson"] = msg_rows[0][1]
            new_eat_lunch_request["food_name"]= msg_rows[1][1]
            new_eat_lunch_request["food_price"] = msg_rows[2][1]
            new_eat_lunch_request["remarks"] = msg_rows[3][1]
            request_data.append(new_eat_lunch_request)
        with open ("lunch.json", "w", encoding='utf-8') as f:
            json.dump(request_data, f, indent=4, ensure_ascii=False)
            
    except (FileNotFoundError, json.JSONDecodeError):
        request_data = {} # 如果檔案不存在或 JSON 格式錯誤，初始化為空 table
        
    # restore_request_data.append(msg_rows)
    # print("JSON 檔案已生成")


@app.route('/eat_lunch_request', methods=['GET'])
def eat_lunch_request():
    salesperson = request.args.get('salesperson','wawaSalesperson:<<<')
    food_name = request.args.get('food_name','wawaFoodName:<<<')
    food_price = request.args.get('food_price','wawaFoodPrice:<<<')
    remarks = request.args.get('remarks','wawaRemarks:<<<')
    
    return jsonify({
        "salesperson": salesperson,
        "food_name": food_name,
        "food_price": food_price,
        "remarks": remarks  
    })


if __name__ == '__main__':
    socketio.run(app,debug=True , port=8080 , host='0.0.0.0' )

