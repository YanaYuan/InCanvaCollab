# InCanva - AI-Powered Document Interface

一个基于Flask和Claude AI的智能文档界面应用，提供类似Canva的可调整容器和AI聊天功能。

## 🚀 功能特性

- **📊 Excel容器** - 可拖拽调整大小的Excel文档界面
- **📝 Word容器** - 可拖拽调整大小的Word文档界面  
- **🤖 Claude AI聊天** - 集成Claude Sonnet 4的智能对话
- **📎 文档附件** - 将选中的文档内容发送给AI
- **🔄 流式响应** - 实时显示AI回复
- **🎨 响应式界面** - 现代化的用户界面设计

## 🛠️ 安装和运行

### 1. 克隆项目
```bash
git clone [your-repo-url]
cd InCanva6
```

### 2. 创建虚拟环境
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. 安装依赖
```bash
pip install flask flask-cors requests python-dotenv
```

### 4. 配置API密钥
```bash
# 复制环境变量模板
cp .env.example .env
# 编辑 .env 文件，填入你的Claude API密钥
```

在`.env`文件中配置：
```
API_KEY=your_claude_api_key_here
BASE_URL=https://www.dmxapi.cn/v1
```

### 5. 运行应用
```bash
python server.py
```

访问 http://localhost:5000 即可使用应用。

## 📝 API密钥获取

1. 访问 [Claude API提供商](https://www.dmxapi.cn)
2. 注册账户并获取API密钥
3. 将密钥配置到`.env`文件中

## 🔒 安全说明

- **切勿**将`.env`文件提交到Git仓库
- 使用`.env.example`作为配置模板
- API密钥仅存储在本地环境变量中

## 📱 使用方法

1. **容器操作**: 拖拽容器边缘调整大小和位置
2. **AI对话**: 在聊天框中输入消息与Claude对话
3. **文档附件**: 选择文档内容后发送给AI分析
4. **文档创建**: AI回复中的Excel/Word内容会自动创建对应容器

## 🚀 Vercel部署

### 一键部署到Vercel
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/[your-username]/InCanva6)

### 手动部署步骤
1. 将代码推送到GitHub
2. 在Vercel中导入GitHub仓库
3. 在Vercel环境变量中设置：
   - `API_KEY`: 你的Claude API密钥
   - `BASE_URL`: https://www.dmxapi.cn/v1
4. 点击部署

### 环境变量配置
在Vercel Dashboard中设置以下环境变量：
```
API_KEY=your_claude_api_key_here
BASE_URL=https://www.dmxapi.cn/v1
```

## 🧰 技术栈

- **后端**: Flask, Flask-CORS
- **前端**: HTML5, CSS3, JavaScript
- **AI**: Claude Sonnet 4 API
- **环境管理**: python-dotenv
- **部署**: Vercel Serverless Functions

## 📄 项目结构

```
InCanva6/
├── server.py          # Flask后端服务器
├── index.html         # 前端界面
├── .env              # 环境变量（本地）
├── .env.example      # 环境变量模板
├── .gitignore        # Git忽略文件
├── README.md         # 项目说明
└── .venv/           # 虚拟环境
```

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目！

## 📄 许可证

[MIT License](LICENSE)
1. 安装Python依赖:
   ```bash
   pip install -r requirements.txt
   ```

2. 启动后端服务:
   ```bash
   python server.py
   ```

3. 在浏览器中打开 `index.html` 文件

## 功能说明

- **实时AI对话**: 与Claude Sonnet 4进行自然语言对话
- **文档拖拽**: 可以拖拽Excel和Word文档容器
- **文档选择**: 使用复选框选择文档
- **AI输出展示**: 当AI生成代码或HTML内容时，会在Claude输出容器中显示
- **快捷键**: 
  - `Ctrl+A`: 选择所有文档
  - `Escape`: 取消所有选择
  - `Enter`: 发送消息

## API配置

后端服务使用了Claude Sonnet 4 API，配置信息在 `server.py` 文件中。

## 注意事项

- 确保后端服务正在运行才能使用聊天功能
- 聊天输入框的占位符会显示当前连接状态
- 如果连接失败，请检查后端服务是否正常运行

## 技术栈

- 前端: HTML5, CSS3, JavaScript
- 后端: Python Flask
- AI: Claude Sonnet 4 API
