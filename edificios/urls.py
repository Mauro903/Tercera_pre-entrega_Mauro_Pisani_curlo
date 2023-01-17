from edificios.views import *

from django.urls import path


urlpatterns = [
    path('bienvenidos/', bienvenidos, name='bienvenidos'),
    path('edificios/', listar_edificios, name='listar_edificios'),
    path('inquilinos/', listar_inquilinos, name='listar_inquilinos'),
    path('encargados/', listar_encargados, name= 'listar_encargados'),
    path('crear-inquilinos/', crear_inquilino, name='crear_inquilinos'),
    path('buscar-encargado/', buscar_encargado, name='buscar_encargado'),
    path('inquilinos/<int:id>/', ver_inquilinos, name='ver_inquilinos'),
    path('editar-inquilinos/<int:id>/', editar_inquilino, name='editar_inquilino'),
    path('eliminar-inquilinos/<int:id>/', eliminar_inquilino, name='eliminar_inquilino'),
]
