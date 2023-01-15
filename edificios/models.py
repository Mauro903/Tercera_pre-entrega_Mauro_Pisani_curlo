from django.db import models

# Create your models here.
class Inquilino(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(null=True) #El null=True es para no tener que completarlo
    edificio = models.CharField(max_length= 30)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}" #Para que en el queryset, me diga directamente los strings de los objetos

class Edificio(models.Model):
    nombre = models.CharField(max_length=30) #Caracteres
    direccion = models.CharField(max_length=160)
    encargado= models.CharField(max_length=32)
    telefono = models.IntegerField()
    #bio = models.TextField(null=True) Archivo de texto que no tiene limites

    def __str__(self):
        return f"{self.nombre}, {self.direccion}"
