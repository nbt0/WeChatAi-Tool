# 数据库配置
DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'database': 'wechat_ai',
    'user': 'root',
    'password': '请替换为实际密码'
}

# 微信公众号配置
WECHAT_CONFIG = {
    'app_id': '请替换为实际APP_ID',
    'app_secret': '请替换为实际APP_SECRET',
    'token': '请替换为实际Token'
}

# AI服务配置（以讯飞星火为例）
AI_CONFIG = {
    'app_id': '请替换为实际APP_ID',
    'api_key': '请替换为实际API_KEY',
    'api_secret': '请替换为实际API_SECRET'
}

# APScheduler配置
SCHEDULER_CONFIG = {
    'timezone': 'Asia/Shanghai',
    'job_defaults': {
        'coalesce': False,
        'max_instances': 1
    }
}

# 静态资源配置
STATIC_FOLDER = 'static'
WEIGHT_CHARTS_FOLDER = f'{STATIC_FOLDER}/weight_charts'