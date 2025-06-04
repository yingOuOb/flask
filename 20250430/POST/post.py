from flask import Flask, request, jsonify,render_template
app = Flask(__name__)
@app.route('/post_example', methods=['POST'])
def post_example():
    data = request.get_json()
    name = data.get('name', 'Guest')
    return jsonify({'message': f'Hello, {name}! This is a POST request.'})
@app.route('/', methods=['GET'])
def index():
    return render_template('post.html')  # 返回 HTML 頁面
app.run(debug=True)