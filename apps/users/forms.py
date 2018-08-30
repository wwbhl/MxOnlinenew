# -*- encoding:utf-8 -*-

__author__ = 'baohailong'
__data__ = '2018/8/30 3:59 PM'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)