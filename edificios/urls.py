from edificios.views import bienvenidos, listar_inquilinos, listar_edificios
from django.urls import path


urlpatterns = [
    path("bienvenidos/", bienvenidos),
    path("inquilinos/", listar_inquilinos),
    path("edificios/", listar_edificios),
]
