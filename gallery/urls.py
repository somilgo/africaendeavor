from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^upload/$', views.upload, name='upload'),
	url(r'^(?P<pk>[0-9]+)/$', views.item_detail, name = 'item_detail'),
]