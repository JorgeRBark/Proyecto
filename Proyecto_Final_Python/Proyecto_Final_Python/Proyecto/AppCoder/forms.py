from django import forms


class FromularioEjercicio (forms.Form):
    nombre = forms.CharField(max_length=40)
    vueltas = forms.IntegerField()
    repeticiones = forms.IntegerField()

class FromularioProfesores (forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)

class FromularioEstudiantes (forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    telefono = forms.IntegerField()


class Busqueda (forms.Form):
    nombre  = forms.CharField(max_length=40, required=False)