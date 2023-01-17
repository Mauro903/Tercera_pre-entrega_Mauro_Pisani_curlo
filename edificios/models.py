from django.db import models

# Create your models here.
class Inquilino(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nacimiento = models.DateField(null=True) #El null=True es para no tener que completarlo
    edificio = models.CharField(max_length= 30)
    descripcion = models.CharField (max_length=200)
   

    def __str__(self):
        return f"{self.apellido}, {self.nombre}, {self.edificio}" #Para que en el queryset, me diga directamente los strings de los objetos

class Edificio(models.Model):
    nombre = models.CharField(max_length=30) 
    direccion = models.CharField(max_length=160)
    encargado= models.CharField(max_length=32)
    telefono = models.IntegerField()


    def __str__(self):
        return f"{self.nombre}, {self.direccion}, {self.encargado}"

class Encargado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=32)
    antiguedad = models.CharField(max_length=100)
    edificio = models.CharField(max_length= 30)
    
    def __str__(self):
        return f"{self.nombre}, {self.edificio}, {self.antiguedad} "