from django.db import models
import random
from django.utils import timezone
#设置默认签名

# random_sign = random.choice(['stay hungry,stay foolish!','talk is checp,show me code','never give up'])
def default_sign():
    signs =['stay hungry,stay foolish!','never give up','every day need make up']
    return random.choice(signs)

def default_info():
    sign =['stay hungry,stay foolish!','never give up','every day need make up']
    return random.choice(sign)


# Create your models here.
class UserProfile(models.Model):


    username =models.CharField(max_length=11,verbose_name='用户名',primary_key=True)
    nickname =models.CharField(max_length=50,verbose_name='昵称')
    email =models.EmailField()
    password =models.CharField(max_length=32)
    sign =models.CharField(max_length=50,verbose_name='个人签名',default =default_sign)
    #default 可以直接引用函数名
    info =models.CharField(max_length=150,verbose_name='个人简介',default =default_info)
    avatar =models.ImageField(upload_to='Avatar',null=True)
    #from django.utils import timezone  djanog 数据库存的是utc
    #新增datetime字段时，给default
    created_time =models.DateTimeField(default=timezone.now)
    #created_time =models.DateTimeField(auto_now_add =True.default =0.0)
    updated_time =models.DateTimeField(default =timezone.now)
    phone =models.CharField(max_length=11,default='')


    class Meta:
        db_table ='user_user_profile'


    