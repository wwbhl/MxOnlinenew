# -*- encoding:utf-8 -*-

__author__ = 'baohailong'
__data__ = '2018/9/5 9:20 AM'

from django.conf.urls import url, include
from .views import CourseListView, CourseDetailView

urlpatterns = [
    #课程列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),

    #课程详情页
    url(r'^detail/(?P<course_id>\d+)$', CourseDetailView.as_view(), name='course_detail'),

]