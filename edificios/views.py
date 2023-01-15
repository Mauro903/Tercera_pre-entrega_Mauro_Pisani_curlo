from django.shortcuts import render
from django.http import HttpResponse

from edificios.models import Edificio, Inquilino

def bienvenidos(request):
    return HttpResponse("Bienvenidos a consorcios mengano")
# Create your views here.

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


