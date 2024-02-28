from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import FromularioEjercicio,  FromularioProfesores, FromularioEstudiantes, Busqueda

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return render(request,"AppCoder/index.html")


def formulario_ejercicio(request):
    
      if request.method == "POST":
 
            formejercicio = FromularioEjercicio(request.POST) # Aqui me llega la informacion del html
            print(formejercicio)
 
            if formejercicio.is_valid():

                  informacion = formejercicio.cleaned_data
                  ejercicios = Ejercicio (nombre=informacion['nombre'], vueltas=informacion['vueltas'], repeticiones=informacion['repeticiones'])
                  ejercicios.save()
                  return render(request, "AppCoder/ejercicios.html")
      else:
        formejercicio = FromularioEjercicio()
 
      return render(request, "AppCoder/ejercicios.html", {"formejercicio": formejercicio})

def formulario_profesores(request):
    
      if request.method == "POST":
 
            formprofesores = FromularioProfesores(request.POST) # Aqui me llega la informacion del html
            print(formprofesores)
 
            if formprofesores.is_valid():

                  informacion = formprofesores.cleaned_data
                  profesores = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'])
                  profesores.save()
                  return render(request, "AppCoder/profesores.html")
      else:
        formprofesores = FromularioProfesores()
 
      return render(request, "AppCoder/profesores.html", {"formprofesores": formprofesores})

def formulario_estudiantes(request):
    
      if request.method == "POST":
 
            formestudiantes = FromularioEstudiantes(request.POST) # Aqui me llega la informacion del html
            print(formestudiantes)
 
            if formestudiantes.is_valid():

                  informacion = formestudiantes.cleaned_data
                  estudiantes = Estudiante (nombre=informacion['nombre'], apellido=informacion['apellido'], telefono=informacion['telefono'])
                  estudiantes.save()
                  return render(request, "AppCoder/estudiantes.html")
      else:
        formestudiantes = FromularioEstudiantes()
 
      return render(request, "AppCoder/estudiantes.html", {"formestudiantes": formestudiantes})

def formulario_busqueda(request):
    
      if request.method == "POST":
 
            formbusqueda = Busqueda(request.POST) 
 
            if formbusqueda.is_valid():

                  informacion = formbusqueda.cleaned_data
                  nombre = informacion.get('nombre')
                  estudiantes = Estudiante.objects.filter(nombre__icontains=nombre)
                 
                  return render(request, "AppCoder/busqueda.html", {"estudiantes": estudiantes})
      else:
        formbusqueda = Busqueda()

      return render(request, "AppCoder/busqueda.html", {"formbusqueda": formbusqueda})