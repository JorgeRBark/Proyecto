from django.contrib import admin
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio),
    path('/estudiantes', views.estudiantes),
    path('/ejercicios', views.ejercicios),
]