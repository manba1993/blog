import hashlib

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from user.models import UserProfile
import json
from django.conf import settings
import time
import jwt

#10200 - 10299异常码范围
# Create your views here.
class TokenView(View):

    def post(self,request):

        #获取用户名和密码


        json_str =request.body
        json_obj =json.loads(json_str)

        username =json_obj['username']
        password =json_obj['password']

        # 检验用户名和密码
        try:
            user =UserProfile.objects.get(username=username)
        except Exception as e:
            print('---login error is %s'%(e))
            result ={'code':10200,"error":'Your username or password is wrong' }
            return JsonResponse(result)

        h_m =hashlib.md5()
        h_m.update(password.encode())
        if h_m.hexdigest() != user.password:
            result = {'code': 10201, "error": 'Your username or password is wrong'}
            return JsonResponse(result)

        # 检验成功后，签发token  有限期1天
        token =make_token(username)

        result ={'code':200,'username':username,'data':{'token':token.decode()}}
        return JsonResponse(result)

def make_token(username,expire =3600*24):
    key =settings.JWT_TOKEN_KEY
    now =time.time()
    payload ={'username':username,'exp':now+expire}
    return jwt.encode(payload,key,algorithm='HS256')