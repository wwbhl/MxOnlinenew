# -*- encoding:utf-8 -*-

__author__ = 'baohailong'
__data__ = '2018/9/7 5:01 PM'

from django.conf.urls import url, include
from .views import UserInfoView, UploadImageView, UpdatePwdView

urlpatterns = [
    #用户信息
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),
    #用户头像上传
    url(r'^image/upload/$', UploadImageView.as_view(), name='image_upload'),
    #用户个人中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name='update_pwd'),
]