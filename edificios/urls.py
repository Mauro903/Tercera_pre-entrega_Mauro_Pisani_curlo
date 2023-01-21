from edificios.views import *


from django.urls import path


urlpatterns = [
    path('bienvenidos/', bienvenidos, name='bienvenidos'),
    #URLS (basadas en views funcionales)
    path('edificios/', listar_edificios, name='listar_edificios'),
    #path('inquilinos/', listar_inquilinos, name='listar_inquilinos')
    path('encargados/', listar_encargados, name= 'listar_encargados'),
    #path('crear-inquilinos/', crear_inquilino, name='crear_inquilinos'),
    path('buscar-encargado/', buscar_encargado, name='buscar_encargado'),
    #path('inquilinos/<int:id>/', ver_inquilinos, name='ver_inquilinos'),
    #path('editar-inquilinos/<int:id>/', editar_inquilino, name='editar_inquilino'),
    #path('eliminar-inquilinos/<int:id>/', eliminar_inquilino, name='eliminar_inquilino'),
    #URLS basadas en class based viwes, vistas basadas en clases
    path('inquilinos/', InquilinoListView.as_view(), name='listar_inquilinos'),
    path('crear-inquilinos/', InquilinoCreateView.as_view(), name='crear_inquilinos'),
    path('eliminar-inquilinos/<int:pk>/', InquilinoDeleteView.as_view(), name='eliminar_inquilino'),
    path('editar-inquilinos/<int:pk>/', InquilinoUpdateView.as_view(), name='editar_inquilino'),
    path('inquilinos/<int:pk>/', InquilinoDetailView.as_view(), name='ver_inquilino'),
]
