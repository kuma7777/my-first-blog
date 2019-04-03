from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # post_listをルートURLに割り当て
    path('post/<int:pk>)/', views.post_detail, name='post_detail'), # pkに数字が入る
]