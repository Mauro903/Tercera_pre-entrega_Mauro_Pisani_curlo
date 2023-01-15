from django.shortcuts import render
from django.http import HttpResponse

def bienvenidos(request):
    return HttpResponse("Bienvenidos a consorcios mengano")
# Create your views here.

def listar_inquilinos(request):
    return render(request=request, template_name="edificios/lista_inquilinos.html")
    