from django.db import models
from django.db.models.fields import TextField

# Create your models here.

class Servicio(models.Model):
    codigoIdentificador = models.CharField(max_length=15, primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    

class Proveedor(models.Model):
    
    rut = models.CharField(max_length=15, primary_key=True)
    razonSocial = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    tipoServicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)

    def __str__(self):
        return self.rut