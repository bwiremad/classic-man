from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from . import  views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^registered/$', views.registered, name='registered'),

    url(r'^accounts/login/$', login, {'template_name':'account/login.html'}),
    url(r'^accounts/logout/$', logout, {'template_name':'account/loggedout.html'}),


]
