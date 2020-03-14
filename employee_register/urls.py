from django.contrib import admin
from django.urls import path, include
from . import views 

app_name = 'user' 

urlpatterns = [
    path('list', views.employee_list, name='list'), 
    path('delete/<int:id>/' , views.employee_delete, name='delete'), 
    path('', views.employee_form, name='insert'),
    path('<int:id>/', views.employee_form,name='update'), # get and post req. for update operation
]
