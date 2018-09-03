# -*- encoding:utf-8 -*-

__author__ = 'baohailong'
__data__ = '2018/9/3 8:40 PM'

from django.conf.urls import url, include
from .views import OrgView, AddUserAskView

urlpatterns = [
    #课程机构列表页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask')
]