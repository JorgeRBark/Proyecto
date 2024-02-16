from django.db import models

# Create your models here.


class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    

class Ejercicio(models.Model):
    nombre = models.CharField(max_length=40)
    vueltas = models.IntegerField()
    repeticiones = models.IntegerField()
