from django.shortcuts import render, redirect

from django.urls import reverse, reverse_lazy

from edificios.models import *
from edificios.forms import *
from django.db.models import Q
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def bienvenidos(request):
        return render(
        request=request,
        template_name="edificios/inicio.html",
    )


#def listar_inquilinos(request):
 #   contexto = {
  #      "inquilino": Inquilino.objects.all()
 #   }
 #   return render(
 #       request=request,
  #      template_name="edificios/lista_inquilinos.html",
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

#def crear_inquilino(request):
   # if request.method == "POST":
     #   formulario = InquilinoFormulario(request.POST)

      #  if formulario.is_valid():
       #     data = formulario.cleaned_data
       #     inquilino= Inquilino(
       #     nombre= data["nombre"],
        #    apellido= data["apellido"],
       #     dni= data["dni"],
       #     email= data["email"],
       #     fecha_nacimiento= data["fecha_nacimiento"], 
       #     edificio= data["edificio"])
        #    inquilino.save()
       #     url_exitosa = reverse("listar_inquilinos")
       #     return redirect(url_exitosa)
  #  else:
      #  formulario = InquilinoFormulario()
     #   return render(
    #        request=request,
    #        template_name="edificios/formulario_inquilinos.html",
    #        context={"formulario":  formulario},
     #   )

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

#def ver_inquilinos(request, id):
  #  inquilino = Inquilino.objects.get(id=id)
 #   contexto = {
  #          "inquilino": inquilino
 #   }
  #  return render(
  #      request=request,
  #      template_name="edificios/detalle_inquilino.html",
  #      context=contexto,
  #  )

#def editar_inquilino(request, id):
  #  inquilino = Inquilino.objects.get(id=id)
   # if request.method == "POST":
   #     formulario = InquilinoFormulario(request.POST)


   #     if formulario.is_valid():
    #        inquilino.nombre= data["nombre"]
    #        inquilino.apellido= data["apellido"]
    #        inquilino.descripcion = data["descripcion"]
    #        inquilino.dni= data["dni"],
    #        inquilino.email= data["email"],
    #        inquilino.fecha_nacimiento= data["fecha_nacimiento"], 
    #        inquilino.edificio= data["edificio"]
    #        inquilino.descripcion= data["descripcion"]
    #        inquilino.save()
    #        url_exitosa = reverse("listar_inquilinos")
    #        return redirect(url_exitosa)
    #    else:
    #        inicial={
    #            "nombre": inquilino.nombre,
    #            "apellido": inquilino.apellido,
    #            "descripcion": inquilino.descripcion,
     #       }
    #        formulario = InquilinoFormulario(initial=inicial)
    #    return render(
    #        request=request,
    #        template_name="edificios/formulario_inquilinos.html",
    #        context={"formulario":  formulario, "inquilino": inquilino, "es_update":True},
     #   )

#def eliminar_inquilino(request, id):
#    inquilino = Inquilino.objects.get(id=id)
#    if request.method =="POST":
#        inquilino.delete()
#        url_exitosa = reverse("listar_inquilinos")
#        return redirect(url_exitosa)



class InquilinoListView(LoginRequiredMixin, ListView):
    model = Inquilino
    template_name = "edificios/lista_inquilinos.html"


class InquilinoCreateView(LoginRequiredMixin, CreateView):
    model = Inquilino
    fields = ['nombre', 'apellido', 'dni', 'email','fecha_nacimiento', 'edificio', 'descripcion']
    success_url = reverse_lazy('listar_inquilinos')
    template_name = "edificios/formulario_inquilinos.html"


class InquilinoDetailView(LoginRequiredMixin, DetailView):
    model = Inquilino
    success_url = reverse_lazy('listar_inquilinos')
    template_name = "edificios/detalle_inquilino.html"


class InquilinoUpdateView(LoginRequiredMixin, UpdateView):
    model = Inquilino
    fields = ['nombre', 'apellido', 'dni', 'email','fecha_nacimiento', 'edificio', 'descripcion']
    success_url = reverse_lazy('listar_inquilinos')
    template_name = "edificios/formulario_inquilinos.html"


class InquilinoDeleteView(LoginRequiredMixin, DeleteView):
    model = Inquilino
    success_url = reverse_lazy('listar_inquilinos')
    template_name = "edificios/confirmar_eliminacion_inquilino.html"

def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()  # Esto lo puedo usar porque es un model form
            url_exitosa = reverse('bienvenidos')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='edificios/registro.html',
        context={'form': formulario},
    )


def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('bienvenidos')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='edificios/login.html',
        context={'form': form},
    )


class CustomLogoutView(LogoutView):
    template_name = 'edificios/logout.html'

#class ProfilUpdateView(LoginRequiredMixin, UpdateView):
   # model = User
   # from_class = UserUpdateForm
   # success_url = reverse_lazy("inicio")
    #template_name = "edificios/formulario_perfil.html"

   # def get_object(self, queryset=none):
   #                return.self.request_user
  