from edificios.views import bienvenidos, listar_inquilinos, listar_edificios, listar_encargados
from django.urls import path


urlpatterns = [
    path("bienvenidos/", bienvenidos, name="bienvenidos"),
    path("edificios/", listar_edificios, name="listar_edificios"),
    path("inquilinos/", listar_inquilinos, name="listar_inquilinos"),
    path("encargados/", listar_encargados, name= "listar_encargados"),
]
