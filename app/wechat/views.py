from flask import request, Blueprint

wechat_bp = Blueprint('wechat', __name__)

@wechat_bp.route('/wechat', methods=['GET', 'POST'])
def wechat():
    """处理微信服务器的消息请求"""
    if request.method == 'GET':
        # 处理服务器配置验证
        return ''
    else:
        # 处理微信消息
        return ''