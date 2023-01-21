from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class InquilinoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    dni = forms.CharField(max_length=32)
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField(required=True) 
    edificio = forms.CharField(max_length= 30)
    descripcion = forms.CharField(required=False, max_length= 2000000)

class UserRegisterForm(UserCreationForm):
    #Esto es un ModelForm
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ["last_name", "first_name", "username", "email", "password1", "password2"]