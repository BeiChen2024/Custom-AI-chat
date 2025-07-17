```python
from flask import Flask, render_template, request, jsonify
from chatbot import ChatBot
import os
import json

app = Flask(__name__)

# 加载配置
config_path = os.path.join(os.path.dirname(__file__), '../config/config.json')
with open(config_path, 'r') as f:
    config = json.load(f)

# 初始化聊天机器人
chatbot = ChatBot(
    api_key=config['api_key'],
    model_url=config['model_url'],
    model_name=config['model_name'],
    temperature=config['temperature'],
    max_tokens=config['max_tokens']
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = chatbot.generate_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
```
