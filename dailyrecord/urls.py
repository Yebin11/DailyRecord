from django.urls import path

from . import views

app_name = 'daily_record'

urlpatterns = [
    path('', views.index),
    path('login/', views.loginP),
    path('login/findInfo/', views.findInfoP),
    path('join/', views.joinP),
    path('header/', views.header, name='header'),
    path('mypage/', views.mypage, name='mypage'),
    path('pw_reset/', views.pw_reset, name='pw_reset'),
    path('calendar/', views.calendar, name='calendar'),
]