from edificios.views import bienvenidos
from django.urls import path


urlpatterns = [
    path("bienvenidos/", bienvenidos),
]
