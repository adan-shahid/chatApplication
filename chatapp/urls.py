from django.contrib import admin
from django.urls import path, include
from chatapp import views

urlpatterns = [
    path('', views.index, name='index'),
    
]
