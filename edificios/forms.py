from django import forms

class InquilinoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    dni = forms.CharField(max_length=32)
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField(required=True) 
    edificio = forms.CharField(max_length= 30)
    descripcion = forms.CharField(required=False, max_length= 2000000)