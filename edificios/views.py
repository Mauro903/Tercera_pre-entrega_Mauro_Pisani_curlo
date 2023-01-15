from django.shortcuts import render
from django.http import HttpResponse

from edificios.models import Edificio, Inquilino, Encargado

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
