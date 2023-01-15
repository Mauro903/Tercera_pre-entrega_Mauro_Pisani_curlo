from django.shortcuts import render
from django.http import HttpResponse

def bienvenidos(request):
    return HttpResponse("Bienvenidos a consorcios mengano")
# Create your views here.
