from django.shortcuts import render, redirect

from django.urls import reverse

from edificios.models import *
from edificios.forms import *

def bienvenidos(request):
        return render(
        request=request,
        template_name="edificios/inicio.html",
    )


def listar_inquilinos(request):
    contexto = {
        "inquilino": Inquilino.objects.all()
    }
    return render(
        request=request,
        template_name="edificios/lista_inquilinos.html",
        context=contexto,
    )

def listar_edificios(request):
    contexto= {
        "edificios": Edificio.objects.all()
    }
    return render(
        request=request,
        template_name="edificios/lista_edificios.html",
        context=contexto,
    )

def listar_encargados(request):
    contexto= {
        "edificios": Encargado.objects.all()
    }
    return render(
        request=request,
        template_name="edificios/lista_encargados.html",
        context=contexto,
    )

def crear_inquilino(request):
    if request.method == "POST":
        formulario = InquilinoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            inquilino= Inquilino(
            nombre= data["nombre"],
            apellido= data["apellido"],
            dni= data["dni"],
            email= data["email"],
            fecha_nacimiento= data["fecha_nacimiento"], 
            edificio= data["edificio"])
            inquilino.save()
            url_exitosa = reverse("listar_inquilinos")
            return redirect(url_exitosa)
    else:
        formulario = InquilinoFormulario()
        return render(
            request=request,
            template_name="edificios/formulario_inquilinos.html",
            context={"formulario":  formulario},
        )
