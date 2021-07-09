from django.urls import path

from . import views

app_name = 'daily_record'

urlpatterns = [
    path('', views.index),
    path('login/', views.loginP),
    path('join/', views.joinP),
    path('header/', views.header, name='header')
]
