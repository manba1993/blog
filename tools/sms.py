import datetime
import hashlib
import base64
import requests   # 用该库发出http请求
import json

class YunTongXin():
    base_url = 'https://app.cloopen.com:8883'

    def __init__(self, accountSid, accountToken,appId,templateId):
        self.accountSid = accountSid
        self.accountToken = accountToken
        self.appId =appId
        self.templateId =templateId
    # 构造url

    def get_request_url(self, sig):
        self.url = self.base_url + '/2013-12-26/Accounts/%s/SMS/TemplateSMS?sig=%s' % (self.accountSid, sig)
        return self.url

    def get_timestamp(self):
        # 生成时间戳
        # 时间戳是当前系统时间，格式"yyyyMMddHHmmss"。时间戳有效时间为24小时，如：               20140416142030
        now = datetime.datetime.now()
        now_str = now.strftime('%Y%m%d%H%M%S')
        return now_str

    def get_sig(self, timestamp):
        # 1.使用MD5加密（账户Id + 账户授权令牌 + 时间戳）。其中账户Id和账户授权令牌根据         url的验证级别对应主账户。
        s = self.accountSid + self.accountToken + timestamp
        m = hashlib.md5()
        m.update(s.encode())

        # 2
        # SigParameter  参数需要大写，如不能写成Sig =abcdefg 而应该写成sig =ABCDEFG
        return m.hexdigest().upper()

    def get_request_header(self, timestamp):
        # 构建请求头
        # 1.使用Base64编码（账户Id + 冒号 + 时间戳）其中账户Id根据url的验证级别对应主账户
        # 2.冒号为英文冒号
        # 3.时间戳是当前系统时间，格式"yyyyMMddHHmmss"，需与SigParameter中时间戳相同。
        s = self.accountSid + ':' + timestamp
        b_s = base64.b64encode(s.encode()).decode()
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json;charset =utf-8',
            'Authorization':b_s
        }

    def get_request_body(self, phone, code):
        # 构建请求体
        data = {
            'to': phone,
            'appId': self.appId,
            'templateId': self.templateId,
            'datas': [code, '3']
        }
        return data

    def do_request(self,url,header,body):
        #发http请求
        res =requests.post(url,headers =header,data =json.dumps(body))     #发post 请求
        return res.text



    def run(self,phone,code):
        # 第一部分url
        timestamp = self.get_timestamp()
        sig = self.get_sig(timestamp)
        url = self.get_request_url(sig)
        header =self.get_request_header(timestamp)
        body =self.get_request_body(phone,code)
        res =self.do_request(url,header,body)
        return res
        #print(url)


if __name__ == '__main__':
    aid = '8a216da8730e55c101731252cf48019d'
    atoken = 'dbe163c14a424f039bcd95d90ec5912a'
    appId ='8a216da8730e55c101731252d03501a3'
    tid ='1'

    x = YunTongXin(aid, atoken,appId,tid)
    res =x.run('18297963825.py'
               '','120116')
    print(res)