from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)  # 將 SocketIO 實例綁定到 Flask 應用

# 路由處理
@app.route('/')
def index():
    return render_template('index.html')     # 返回 HTML 頁面

# 當接收到客戶端的消息時，處理它
@socketio.on('to_back_message')  # 當收到前端傳送的 'chat message' 事件時
def handle_message(msg):
    print(f'Received message: {msg}')   # cmd print
    emit('to_front_message', msg, broadcast=True)  # 向所有客戶端廣播消息   #傳送到前端

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)  # 使用 SocketIO 運行 Flask 應用
