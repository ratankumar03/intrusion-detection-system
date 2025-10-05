# sniffer/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    # path('',views.test),
     path('', views.index, name='index'),
    path('capture/', views.capture_packets, name='capture_packets'),
    path('home', views.home),
    path('show', views.show),
    path('show1',views.show1)
]
