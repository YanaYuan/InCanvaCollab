from flask import Flask, request, jsonify, Response, send_file
from flask_cors import CORS
import requests
import json
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

app = Flask(__name__)
CORS(app)  # 允许跨域请求

# API配置
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL', 'https://www.dmxapi.cn/v1')

# 检查API密钥是否存在
if not API_KEY:
    raise ValueError("API_KEY not found in environment variables. Please create a .env file with your API key.")

@app.route('/')
def index():
    """服务主页HTML文件"""
    return send_file('index.html')

@app.route('/health', methods=['GET'])
def health():
    """健康检查端点"""
    return jsonify({'status': 'healthy'})

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        print(f"Received request data: {data}")
        
        user_message = data.get('message', '')
        conversation_history = data.get('history', [])
        
        print(f"User message: {user_message}")
        print(f"Conversation history length: {len(conversation_history)}")
        
        # 构建消息历史
        messages = []
        for msg in conversation_history:
            messages.append({
                "role": msg.get('role', 'user'),
                "content": msg.get('content', '')
            })
        
        # 添加当前用户消息
        messages.append({
            "role": "user",
            "content": user_message
        })
        
        print(f"Sending {len(messages)} messages to API")
        
        # 准备API请求
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": "claude-sonnet-4-20250514",
            "messages": messages,
            "max_tokens": 10000,
            "temperature": 0.7,
            "stream": True  # 启用流式响应
        }
        
        print(f"API payload prepared, making streaming request to {BASE_URL}/chat/completions")
        
        # 定义流式响应生成器
        def generate():
            try:
                # 调用Claude API的流式接口
                response = requests.post(
                    f"{BASE_URL}/chat/completions",
                    headers=headers,
                    json=payload,
                    stream=True,
                    timeout=60
                )
                
                if response.status_code != 200:
                    error_detail = response.text
                    print(f"API Error: {response.status_code} - {error_detail}")
                    yield f"data: {json.dumps({'error': f'API request failed: {response.status_code}'})}\n\n"
                    return
                
                # 处理流式响应
                for line in response.iter_lines():
                    if line:
                        line = line.decode('utf-8')
                        if line.startswith('data: '):
                            data_content = line[6:]  # 移除 'data: ' 前缀
                            
                            if data_content.strip() == '[DONE]':
                                yield f"data: {json.dumps({'done': True})}\n\n"
                                break
                            
                            try:
                                chunk_data = json.loads(data_content)
                                if 'choices' in chunk_data and len(chunk_data['choices']) > 0:
                                    delta = chunk_data['choices'][0].get('delta', {})
                                    if 'content' in delta:
                                        content = delta['content']
                                        yield f"data: {json.dumps({'content': content})}\n\n"
                            except json.JSONDecodeError:
                                # 跳过无法解析的行
                                continue
                                
            except requests.exceptions.Timeout:
                print("Request timeout error")
                yield f"data: {json.dumps({'error': 'Request timeout - please try again'})}\n\n"
            except requests.exceptions.ConnectionError:
                print("Connection error")
                yield f"data: {json.dumps({'error': 'Connection error - please check your internet connection'})}\n\n"
            except Exception as e:
                print(f"Streaming error: {str(e)}")
                import traceback
                traceback.print_exc()
                yield f"data: {json.dumps({'error': f'Server error: {str(e)}'})}\n\n"
        
        return Response(generate(), mimetype='text/plain')
            
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': f'Server error: {str(e)}'
        }), 500

# Vercel需要这个变量
app_instance = app

if __name__ == '__main__':
    print("Starting InCanva Chat Server...")
    print("Server will run on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
