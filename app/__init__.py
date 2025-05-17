from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # 在这里后续会添加配置加载、蓝图注册等初始化操作
    
    return app