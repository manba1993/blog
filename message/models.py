from django.db import models
from topic.models import Topic
from user.models import UserProfile

# Create your models here.
class Message(models.Model):
    #留言/回复
    #一个文章多个评论  与文章表进行关联
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    #与用户表关联，评论是什么说的
    user_profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    content = models.CharField(verbose_name='内容',max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)#当对象第一次被创建时自动设置当前时间(取值:True/False)。
    #parent_message=0 留言，默认值为0,是留言，大于0 回复
    parent_message = models.IntegerField(verbose_name='回复的留言ID',default=0)

