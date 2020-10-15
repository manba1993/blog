from celery import Celery
from django.conf import settings
import os


# 添加环境变量，告知celery该跟哪个django项目

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ddblog.settings') #去找项目同名目录下的ddblog.settings

app =Celery('ddblog')

app.conf.update(

    BROKER_URL ='redis://@127.0.0.1:6379/1'  #配置

)

#告知celery去应用目录下寻找任务函数
app.autodiscover_tasks(settings.INSTALLED_APPS)


