from django.contrib import admin

from edificios.models import Edificio, Inquilino, Encargado

admin.site.register(Edificio)
admin.site.register(Inquilino)
admin.site.register(Encargado)
# Register your models here.
