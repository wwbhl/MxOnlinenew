# -*- encoding:utf-8 -*-

__author__ = 'baohailong'
__data__ = '2018/9/7 5:01 PM'

from django.conf.urls import url, include
from .views import UserInfoView

urlpatterns = [
    #用户信息
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),
]