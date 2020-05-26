from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
import datetime

class Persona(object):

    def __init__(self, nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido


def Hello(request):
    """first Views"""

    p1=Persona("Profesor Juan","Lopez Sanchez")
    name = "Juan"
    last_name = "Lopez"
    age = 30
    fecha_actual = datetime.datetime.now()
    temas = ["Plantillas", "Modelos", "Vista"]
    empty = []
    """
    doc_externo = open("/home/juan/DjangoProyectos/My_first_proyect/My_first_proyect/html/1-index.html")
    template = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({"name": p1.nombre, "last": p1.apellido, "my_age": age,\
                        "date":fecha_actual,"temas":temas})
    doc = template.render(contexto)
    """
    """loader- para cargar las plantilla se usa cuando el proyecto tiene varias plantillas"""
    """doc_externo = loader.get_template('1-index.html')
    documento = doc_externo.render({"name": p1.nombre, "last": p1.apellido, "my_age": age,\
                        "date":fecha_actual,"temas":temas})
    return HttpResponse(documento)"""
    """para simplificar mas el codigo se necesita del metodo render"""

    return render(request, '1-index.html', {"name": p1.nombre, "last": p1.apellido, "my_age": age,\
                        "date":fecha_actual,"temas":temas})

def Arduino(request):
    """template Arduino"""
    fecha = datetime.datetime.now()
    return render(request, "arduino.html", {"date": fecha})

def Pic(request):
    """template PIC"""
    fecha = datetime.datetime.now()
    return render(request, "PIC.html", {"date":fecha})

def Bye(request):
    """first Views"""
    return HttpResponse("Bye-Bye!")

def date(request):
    """time"""
    fecha_actual = datetime.datetime.now()

    html = """<html>
    <body>
    <h1> Date Time {}</h1>
    </body>
    </html>
    """.format(fecha_actual)
    return HttpResponse(html)

def calculaEdad(request, age, edad):
    """calculation age"""
    #My_age=20
    periodo=edad-2020
    Age_future= age+periodo
    html="""<html><body><h2> En el año {} tendras {} años</h2></body></html>"""\
    .format(edad, Age_future)
    return HttpResponse(html)
