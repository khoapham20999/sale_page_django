from django.contrib import admin
from django.urls import path
from django.conf.urls import url 
from . import views


app_name = 'home'

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'index', views.index, name='index'), 
    url(r'about', views.about, name='about'), 
    # url(r'blog', views.blog, name='blog'), 
    # url(r'contact', views.contact, name='contact'), 
    # url(r'elements', views.elements, name='elements'), 
    # remove service url
    # url(r'main', views.main, name='main'), 
    # url(r'single', views.single, name='single'), 
    # url(r'list', views.list1, name='list'), 
    # url(r'post/(\d+)$', views.post_page, name='post'), 
    url(r'detail/(\d+)$', views.detail, name='detail'), 
    # url(r'login', views.login, name='login')
]
