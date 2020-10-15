from django.core.cache  import cache
from .logging_dec import get_user_by_request


def topic_cache(expire):
    def _topic_cache(func):
        def wrapper(request,*args,**kwargs):
            """
            区分访问者看哪个缓存
            :param request:
            :param args:
            :param kwargs:
            :return:
            """

            #根据查询字符串区分当前业务
            #根据有没有  t_id 查询字符串区分当前哪的时批量数据还是具体某个文章的数据
            if "t_id" in request.GET.keys():  #request.GET是一个类字典对象.keys取出字典的值
                #拿具体文章
                return func(request,*args,**kwargs)
                #*args:位置传参，  **kwargs：关键字传参**kw是关键字参数，kw接收的是一个dict，关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
            ####以下批量获取数据
            ###检查访问者身份
            vistor_name =get_user_by_request(request)
            ###根据访问者身份和博主的关系，生成特定的cache_key
            author_uername =kwargs['author_id']
            if vistor_name == author_uername:   #博主访问自己
                cache_key =  "topic_cache_self_%s"%(request.get_full_path())  #get_full_path():全部的路由
            ###博主访问自己  topic_cache_self_url
            else:
            ###非博主访问  -topic_cache_url
                cache_key = "topic_cache_%s"%(request.get_full_path())
            print("---cache key is %s"%(cache_key))
            res =cache.get(cache_key)#尝试拿缓存
            if res:
                print("---cache in")
                return res
            #尝试获取缓存，如果有return cache,没有走视图return func，存储缓存
            res =func(request,*args,**kwargs)
            cache.set(cache_key,res,expire)
            return res
        return wrapper
    return  _topic_cache

