# coding=utf-8
"""mysite_login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from login import views

# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#
# ]
# 考虑到登录系统属于站点的一级功能，为了直观和更易于接受.
# 这里没有采用二级路由的方式，而是在根路由下直接编写路由条目,同样也没有使用反向解析名（name参数）.
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    # 注册图片验证码
    url(r'^captcha', include('captcha.urls'))
]
