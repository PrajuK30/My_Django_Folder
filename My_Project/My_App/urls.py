from django.contrib import admin
from django.urls import path
from My_App import views

urlpatterns = [
    path('', views.home, name="home"),  # For the root URL
    path('home1', views.home1, name="home1"),  # For /home1
    path('home2', views.home2, name="home2"),  # For /home2
    path('home3', views.home3, name="home3"),  # For /home3
]
