from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index', views.index, name='index'),
    path('services', views.services, name='services'),
    path('contacts', views.contacts, name='contacts'),
    path('about', views.about, name='about'),
    path('register', views.register, name='register'),
    path('login', views.LoginUser.as_view(), name='login'),
]
