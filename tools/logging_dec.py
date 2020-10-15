from django.http import JsonResponse
import jwt
from django.conf import settings

from user.models import UserProfile


def logging_check(func):
    def wrap(request,*args,**kwargs):
        #请求头  - Authorization
        #request.META.get:拿请求头
        token =request.META.get('HTTP_AUTHORIZATION')
        #检验是否有token
        if not token:
            result ={'code':403,'error':'Please login'}
            return JsonResponse(result)
        #校验Token
        try:
            res = jwt.decode(token,settings.JWT_TOKEN_KEY,algorithm='HS256')
        except Exception as e:
            print('--check login error %s'%(e))
            result = {'code': 403, 'error': 'Please login'}
            return JsonResponse(result)
        username =res['username']
        user =UserProfile.objects.get(username =username)
        request.myuser =user   #赋予request.myuser用户名

        #request.myuser =user(orm查询得到）

        return func(request,*args,**kwargs)
    return wrap


#新建一个方法检测 当前访问者是谁

def get_user_by_request(request):
    token = request.META.get('HTTP_AUTHORIZATION')#request.META.get:拿请求头
    if not token:
        return None

    try:
        res = jwt.decode(token,settings.JWT_TOKEN_KEY)
    except Exception as e:
        print("get_user jwt error %s"%(e))
        return None

    username =res['username']


    #TODO 还要不要查库
    return username