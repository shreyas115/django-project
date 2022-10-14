from django.contrib import admin
from django.urls import path
from . import views

app_name="app1"

urlpatterns =[
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('hi/<name>',views.hiname,name="hi"),
    path('add/<a>/<b>',views.add,name="add"),
    path('tempdemo/',views.tempdemo,name="tempdemo"),
    path('grt2/<a>/<b>',views.grt2,name="grt2"),
    path('homepage/',views.hometemp,name="homepage"),
    path('aboutus/',views.abouttemp,name="aboutus"),
    path('register/',views.register,name="register"),
]