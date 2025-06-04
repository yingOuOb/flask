from flask import Flask, request, render_template_string,render_template,session

app = Flask(__name__)

    
app.config['SECRET_KEY'] = 'random string'

@app.route('/get_example', methods=['GET'])
def get_example():
    if request.args:
        name = request.args.get('name')
        email = request.args.get('email')
        return f'<h2>收到的 GET 資料：</h2><p>姓名：{name}</p><p>電子郵件：{email}</p>'
    return render_template("get.html")

@app.route('/post_example', methods=['GET', 'POST'])
def post_example():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        password = request.form['password']
        return f'<h2>收到的 POST 資料：</h2><p>使用者名稱：{username}</p><p>密碼：{password}</p>'
    return render_template("post.html")

@app.route('/admin')
def profile():
    
    if session.get('username') == "admin":
        return render_template("admin.html")
    else:
        return 'Why are you still here?'

if __name__ == '__main__':
    app.run(debug=True,port=5500)