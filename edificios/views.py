from django.shortcuts import render, redirect

from django.urls import reverse, reverse_lazy

from edificios.models import *
from edificios.forms import *
from django.db.models import Q
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

def bienvenidos(request):
        return render(
        request=request,
        template_name="edificios/inicio.html",
    )


#def listar_inquilinos(request):
   # contexto = {
    #    "inquilino": Inquilino.objects.all()
  #  }
 #   return render(
   #     request=request,
 #       template_name="edificios/lista_inquilinos.html",
 #       context=contexto,
 #   )

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
        "encargado": Encargado.objects.all()
    }
    return render(
        request=request,
        template_name="edificios/lista_encargados.html",
        context=contexto,
    )

def crear_inquilino(request):
    if request.method == "POST":
        formulario = InquilinoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            inquilino= Inquilino(
            nombre= data["nombre"],
            apellido= data["apellido"],
            dni= data["dni"],
            email= data["email"],
            fecha_nacimiento= data["fecha_nacimiento"], 
            edificio= data["edificio"])
            inquilino.save()
            url_exitosa = reverse("listar_inquilinos")
            return redirect(url_exitosa)
    else:
        formulario = InquilinoFormulario()
        return render(
            request=request,
            template_name="edificios/formulario_inquilinos.html",
            context={"formulario":  formulario},
        )

def buscar_encargado(request):
    if request.method == "POST":
        data= request.POST
        encargado = Encargado.objects.filter( 
            Q(nombre__contains=data["busqueda"]) | Q(apellido__exact=data["busqueda"])
        )
    
        contexto = {
            "encargado": encargado
        }
        return render(
            request=request,
            template_name="edificios/lista_encargados.html",
            context=contexto,
        )

def ver_inquilinos(request, id):
    inquilino = Inquilino.objects.get(id=id)
    contexto = {
            "inquilino": inquilino
    }
    return render(
        request=request,
        template_name="edificios/detalle_inquilino.html",
        context=contexto,
    )

def editar_inquilino(request, id):
    inquilino = Inquilino.objects.get(id=id)
    if request.method == "POST":
        formulario = InquilinoFormulario(request.POST)


        if formulario.is_valid():
            data = formulario.cleaned_data
            inquilino.nombre= data["nombre"]
            inquilino.apellido= data["apellido"]
            inquilino.descripcion = data["descripcion"]
            inquilino.dni= data["dni"]
            inquilino.email= data["email"]
            inquilino.fecha_nacimiento= data["fecha_nacimiento"] 
            inquilino.edificio= data["edificio"]
            inquilino.save()
            url_exitosa = reverse("listar_inquilinos")
            return redirect(url_exitosa)
        else:
            inicial={
                "nombre": inquilino.nombre,
                "apellido": inquilino.apellido,
                "descripcion": inquilino.descripcion,
                "dni": inquilino.dni,
                "email":inquilino.email,
                "fecha_nacimiento": inquilino.fecha_nacimiento,
                "edificio": inquilino.edificio,
            }
            formulario = InquilinoFormulario(initial=inicial)
        return render(
            request=request,
            template_name="edificios/formulario_inquilinos.html",
            context={"formulario":  formulario, "inquilino": inquilino, "es_update":True},
        )
def eliminar_inquilino(request, id):
    inquilino = Inquilino.objects.get(id=id)
    if request.method =="POST":
        inquilino.delete()
        url_exitosa = reverse("listar_inquilinos")
        return redirect(url_exitosa)



class EdificiosDetailView(DetailView):
    model = Encargado
    success_url = reverse_lazy('listar_encargados')


class EdificiosUpdateView(UpdateView):
    model = Edificio
    success_url = reverse_lazy('listar_edificios')


class EdificiosDeleteView(DeleteView):
    model = Inquilino
    fields = ['nombre', 'apellido', 'dni', 'email']
    success_url = reverse_lazy('listar_Inquilinos')