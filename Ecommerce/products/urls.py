from django.contrib import admin
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('details/<slug>/', views.details, name='details'),
]