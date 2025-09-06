import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server import app

# Vercel需要的处理函数
def handler(request, response):
    return app(request, response)

# 导出应用实例供Vercel使用
application = app

if __name__ == "__main__":
    app.run()
