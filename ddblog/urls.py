"""ddblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from .import views
from user import views as user_views
from btoken import views as btoken_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_cors',views.test_cors),
    path('test_cors_server',views.test_cors_server),

    #http://127.0.0.1:8000/v1/users[主路由里绑了一个应用的视图]
    #FBV  绑定路由
    #path('v1/users',user_views.users_views)
    #CBV 绑定路由

    path('v1/users',user_views.UsersView.as_view()),  #只要是继承基类的视图类，就会有.as_view()的方法，as_view()会把自己包装成一个function 返回。主路由始终绑的是视图函数，
    path('v1/users/',include('user.urls')) ,              #不带/走path('v1/users',user_views.UsersView.as_view()),带/拆除去走子路由
    path('v1/tokens',btoken_views.TokenView.as_view()),
    path('v1/topics/',include('topic.urls')),
    path('v1/messages/',include('message.url'))
]
#生成一个media_root开头的请求，django 接到后，去settings里的media 文件夹里加载图片
urlpatterns +=static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)