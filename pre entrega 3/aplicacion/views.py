from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

def quienessomos(request):
    return render(request, "aplicacion/Quienes somos.html")

def articulos(request):
    return render(request, "aplicacion/Articulos.html")

def presupuestos(request):
    return render(request, "aplicacion/Presupuestos.html")

def contacto(request):
    return render(request, "aplicacion/Contacto.html")

def contactoform(request):
    if request.metod == "POST":
        contacto = contacto(nombre=request.POST["nombre"], comision=request.POST["comision"])
        contacto.save()
        return HttpResponse(" Se grabo con exito el nuevo contacto")
    
    return render(request, "aplicacion/contactoform.html")

def contactoform2(request):
    miform = contactoform2()
    return render(request, "aplicacion/curso_form2.html", {"form":miform})