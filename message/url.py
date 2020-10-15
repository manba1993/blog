from django.urls import path
from .import views

urlpatterns =[
    #URL : http://127.0.0.1:8000/v1/messages/<topic_id>
    path('<int:topic_id>',views.message_view)
]