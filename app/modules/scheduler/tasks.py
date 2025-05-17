from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from app.modules.scheduler.models import ScheduledTask

scheduler = BackgroundScheduler()

def init_scheduler():
    """初始化定时任务调度器"""
    scheduler.start()
    load_pending_tasks()

def load_pending_tasks():
    """加载待执行的任务"""
    tasks = ScheduledTask.get_pending_tasks()
    for task in tasks:
        schedule_task(task)

def schedule_task(task: ScheduledTask):
    """调度单个任务"""
    scheduler.add_job(
        execute_task,
        'date',
        run_date=task.trigger_time,
        args=[task.id]
    )

def execute_task(task_id: int):
    """执行任务"""
    # TODO: 实现任务执行逻辑
    pass