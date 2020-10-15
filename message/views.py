import json

from django.http import JsonResponse
from django.shortcuts import render
from tools.logging_dec import logging_check
from topic.models import Topic
from .models import Message
# 10400-10499

# Create your views here.
@logging_check
def message_view(request,topic_id):
    if request.method != 'POST':
        result = {'code': 10400, 'error': 'Please use POST'}
        return JsonResponse(result)
    json_str =request.body
    json_obj =json.loads(json_str)
    content =json_obj['content']
    parent_id =json_obj.get('parent_id',0) # 默认值不存在为0

    try:
        topic =Topic.objects.get(id=topic_id)  #取值
    except Exception as e:
        result ={'code':10401,'error':'The topic id is wrong!'}
        return JsonResponse(result)


    user =request.myuser  #赋予request.myuser用户名,取出username
    #存储在mysql
    Message.objects.create(topic=topic,content=content,user_profile =user,parent_message =parent_id)
    return JsonResponse({'code':200})
