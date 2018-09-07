# -*- encoding:utf-8 -*-

__author__ = 'baohailong'
__data__ = '2018/9/3 8:40 PM'

from django.conf.urls import url, include
from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgCDescView, OrgTeacherView, AddFavView
from .views import TeacherListView, TeacherDetailView
urlpatterns = [
    #课程机构列表页
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='org_course'),
    url(r'^desc/(?P<org_id>\d+)/$', OrgCDescView.as_view(), name='org_desc'),
    url(r'^teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name='org_teacher'),
    #机构收藏
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),
    #讲师列表页
    url(r'^teacher/list/$', TeacherListView.as_view(), name='teacher_list'),
    #讲师详情页
    url(r'^teacher/detail/(?P<teacher_id>\d+)/$', TeacherDetailView.as_view(), name='teacher_detail'),
]