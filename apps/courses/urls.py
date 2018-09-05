# -*- encoding:utf-8 -*-

__author__ = 'baohailong'
__data__ = '2018/9/5 9:20 AM'

from django.conf.urls import url, include
from .views import CourseListView

urlpatterns = [
    #课程列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),

]