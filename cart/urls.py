from django.contrib import admin
from django.urls import path
from django.conf.urls import url 
from . import views
from .views import *

app_name = 'cart'

urlpatterns = [
    # url(r'^$', views.cart_detail, name='cart_detail'),
    url('^$', cart_detail.as_view(), name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
    # url('login', loginclass.as_view(), name='login'),
]

