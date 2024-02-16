from django.http import HttpResponse
from django.template import Template, Context, loader


def saludo(request):

    return HttpResponse("Hola Maquita, el viernes unos besitos xfa")



def probando_template(request):
    diccionario = {

    "Bicep": "curl"
}
    plantilla = loader.get_template("template1.html")
    documento =  plantilla.render (diccionario)
    return HttpResponse(documento)