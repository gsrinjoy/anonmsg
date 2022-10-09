from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login',views.logn),
    path('create',views.create),
    path('<str:slugs>',views.send)

    
]