import os
from flask import Flask,render_template,request,render_template_string
from dotenv import load_dotenv

app = Flask(__name__)

@app.route("/")
def slash():
    return "slash:/"

# @app.route('/add/<int:a>')
# def lash():
#     pyb = "514000000" 
#     return render_template("addAAndB.html", b=pyb)

@app.route('/add/<int:a>/<int:b>')  # HTTP method : Path Variables (/5/10) , URL ex : /add/5/10
def add(a, b):
    return f'{a} + {b} = {a+b}'

# @app.route('/querystring')  # HTTP method : Query String (?a=5&b=10) , URL ex : /add?a=5&b=10
# def add(a, b):
#     return f'{a} + {b} = {a+b}'

	
@app.route('/get_example', methods=['GET'])
def get_example():
    if request.args:
        name = request.args.get('name')
        email = request.args.get('email')
        return f'<h2>收到的 GET 資料：</h2><p>姓名：{name}</p><p>電子郵件：{email}</p>'
    return render_template("get.html")


# @app.route("/")
# def slash():
#     return "slash"

# @app.route("/")
# def slash():
#     return "slash"



if __name__ == "__main__":
    load_dotenv()
    app.run(debug=True,port=8080)
    print(os.getenv("a"))
    print(os.getenv("env"))