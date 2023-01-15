from edificios.views import bienvenidos, listar_inquilinos
from django.urls import path


urlpatterns = [
    path("bienvenidos/", bienvenidos),
    path("inquilinos/", listar_inquilinos),
]
