from django.shortcuts import render
from django.http import HttpResponse 
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto
# Create your views here.
def busqueda(request):

    return render(request, "busqueda.html")

def buscar(request):

    if request.GET["producto1"]:
        #mensaje = "Articulo encontrado {}".format(request.GET["producto1"])
        producto = request.GET["producto1"]
        if len(producto) > 24:
            mensaje = "Texto demasiado largo"
        else:    
            articulos = Articulos.objects.filter(nombre__icontains=producto)
            return render(request, "resultado.html", {"articulos":articulos, "query":producto})
    else:
        mensaje = "No ha introducido nada" 
    return HttpResponse(mensaje)

def contacto(request):
    """
    if request.method =="POST":

        subject=request.POST["asunto"]
        message= request.POST["mensaje"] + " " + request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["1213@holbertonschool.com"]
        send_mail(subject, message, email_from, recipient_list)
        return render(request, "gracias.html")
    return render(request, "contacto.html")
    """

    if request.method=="POST":
        miFormulario=FormularioContacto(request.POST)
        if miFormulario.is_valid():
            infForm= miFormulario.cleaned_data
            send_mail(infForm['asunto'], infForm['mensaje'], 
                infForm.get('email',''), ['1213@holbertonschool.com'])
            return render(request,"gracias.html")
    else: 
        miFormulario=FormularioContacto()

    return render(request, "formulario_contacto.html", {"form": miFormulario})
