from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/a")
def hellob():
    appname='Jhon'
    return render_template("index.html",name=appname)


@app.route("/b")
def helloc():
    array=[1,2,4,7,8,20]
    return render_template("Index.html",name=array)


if __name__ == '__main__':
    app.run(debug=True,port=8080)
