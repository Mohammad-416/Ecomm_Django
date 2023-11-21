from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('clients/', views.clients, name='clients'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
    
]