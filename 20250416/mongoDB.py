from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os
app = Flask(__name__)

load_dotenv()
# 設定 MongoDB 連接
app.config["MONGO_URI"] = f"mongodb+srv://aaa:aaa@cluster0.ub2tnqm.mongodb.net/db?retryWrites=true&w=majority&appName=Cluster0"
# mongodb+srv://<db_username>:<db_password>@cluster0.ub2tnqm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
mongo = PyMongo(app)

@app.route("/")
def home():
    # coes = mongo.db.co.insert_one({"a":1})
    # print(coes)
    # for i in coes:
    #     print(i)
    
    return "MongoDB 已連接成功！"

if __name__ == "__main__":
    app.run(debug=True)