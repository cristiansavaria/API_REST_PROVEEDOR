from django.contrib import admin
from .models import Proveedor, Servicio

# Register your models here.

admin.site.register(Servicio)
admin.site.register(Proveedor)
