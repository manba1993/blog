from ddblog.celery import app
from tools.sms import YunTongXin
from django.conf import settings


@app.task
def send_sms(phone,code):
    #把容易阻塞的定义成一个任务
    x = YunTongXin(settings.SMS_ACCOUNT_ID, settings.SMS_ACCOUNT_TOKEN,
                   settings.SMS_APP_ID, settings.SMS_TEMPLATE_ID)
    res = x.run(phone, code)
    return res    # 打印return的值

