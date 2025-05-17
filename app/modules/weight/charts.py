import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from typing import List
from app.modules.weight.models import WeightRecord

def generate_weight_chart(user_id: int, days: int = 30) -> str:
    """生成用户体重变化图表
    
    Args:
        user_id: 用户ID
        days: 统计天数，默认30天
        
    Returns:
        生成的图表文件路径
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    # 获取用户体重记录
    records = WeightRecord.get_user_records(user_id, start_date, end_date)
    if not records:
        return ''
    
    # 准备数据
    dates = [record.record_time for record in records]
    weights = [record.weight for record in records]
    
    # 绘制图表
    plt.figure(figsize=(10, 6))
    plt.plot(dates, weights, 'b-', marker='o')
    plt.title('体重变化趋势')
    plt.xlabel('日期')
    plt.ylabel('体重(kg)')
    plt.grid(True)
    
    # 保存图表
    chart_path = f'static/weight_charts/user_{user_id}_{end_date.strftime("%Y%m%d")}.png'
    plt.savefig(chart_path)
    plt.close()
    
    return chart_path