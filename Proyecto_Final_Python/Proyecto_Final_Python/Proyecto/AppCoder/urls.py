from django.contrib import admin
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name= "inicio"),
    path('estudiantes/', views.formulario_estudiantes, name= "estudiantes"),
    path('ejercicios/', views.formulario_ejercicio, name= 'ejercicios'),
    path('profesores/', views.formulario_profesores, name= 'profesores'),
    path('busqueda/', views.formulario_busqueda, name= 'busqueda'),
    
]