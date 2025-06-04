from flask import Flask, request, jsonify,render_template
app = Flask(__name__)

@app.route('/get_example', methods=['GET'])  
#          ^ 後綴為/get_example就會過來  ^定義這個網址只接受 GET 請求
def get_example():
    name = request.args.get('name', 'Guest')  
    #        ^ name request.args 代表從網址取得參數 (ex: /get_example?name=soupfatfat)   //  default value is 'Guest'
    return jsonify({'message': f'Hello, {name}! This is a GET request.'})
    #       ^ jsonify將dict轉換成json格式，並回傳到前端html

@app.route('/', methods=['GET'])
def home():
    return render_template("get.html")
app.run(debug=True, host='0.0.0.0', port=2000)

