from django.http import HttpResponse
from datetime import datetime
from math import floor
from django.template import Template,Context

def inicio(request):
    archivo = open('D:/actividad04/actividad04/actividad04/template/template1.html')
    template = Template(archivo.read())
    archivo.close()
    contexto = Context()
    template_renderizado = template.render(contexto)

    return HttpResponse(template_renderizado)

def contacto(request):
    nombre = "Luis Andres"
    apellido = "Moloche Garcia"
    fecha = datetime(2003,4,20).date()
    dias = abs((datetime.now().date() - fecha).days)
    edad = floor(dias / 365.25)
    archivo = open('D:/actividad04/actividad04/actividad04/template/template2.html')
    template = Template(archivo.read())
    archivo.close()
    contexto = Context({"nom": nombre, "ape": apellido,"edad": edad})
    template_renderizado = template.render(contexto)

    return HttpResponse(template_renderizado)

def catalogo(request):
    proyectos = ["Python", "JAVA", "SQL", "C#"]
    archivo = open('D:/actividad04/actividad04/actividad04/template/template3.html')
    template = Template(archivo.read())
    archivo.close()
    contexto = Context({"pro": proyectos})
    template_renderizado = template.render(contexto)

    return HttpResponse(template_renderizado)
