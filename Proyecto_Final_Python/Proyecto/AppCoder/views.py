from django.shortcuts import render
from AppCoder.models import *

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return render(request,"index.html")

def estudiantes(request):

    estudiantes = Estudiante.objects.all()
    print(estudiantes)

    return render(request,"Students.html", {"estudiantes": estudiantes})

def ejercicios(request):

    ejercicios = Ejercicio.objects.all()

    return render(request,"ejercicios.html", {"ejercicios": ejercicios})

def profesores(request):

    profesores = Profesor.objects.all()

    return render(request,"profesores.html", {"profesores": profesores})
