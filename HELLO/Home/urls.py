from django.contrib import admin
from django.urls import path
from Home import views
from . import views

##recives the request from hello and gives path
urlpatterns = [
    path("", views.index, name = 'Home'),
    path("About/",views.About, name = 'About'),
    path("service/",views.service, name = 'service'),
    path('contact/', views.ContactView, name='contact'),
   
]