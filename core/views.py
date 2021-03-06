from django.shortcuts import render , redirect, get_object_or_404
import rest_framework
from .models import Proveedor
from.forms import ProveedorForm
from django.contrib import messages
from rest_framework import serializers, viewsets
from .serializers import ProveedorSerializer
from rest_framework.decorators import api_view,permission_classes

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ProveedorViewset(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

    def get_queryset(self):
        proveedor = Proveedor.objects.all()

        rut = self.request.GET.get('rut')

        if rut:
            proveedor = proveedor.filter(rut__contains=rut)

        return proveedor    










def index(request):
    return render(request, 'core/index.html')
def contacto(request):
    return render(request, 'core/contacto.html')
def seccion_gatos(request):
    return render(request, 'core/seccion-gatos.html')
def seccion_perros(request):
    return render(request, 'core/seccion-perros.html')
def formulario_enviado(request):
    return render(request, 'core/formulario-enviado.html')

def agregar_proveedor(request):
    return render(request, 'core/proveedor/agregar.html')


def agregar_proveedor(request):

    data = {
        'form': ProveedorForm()
    }

    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Proveedor agregado exitosamente")
            return redirect(to="listar-proveedor")
        else:
            data["form"] = formulario    


    return render(request, 'core/proveedor/agregar.html', data)

def listar_proveedor(request):
    proveedor = Proveedor.objects.all()

    data = {
        'proveedor': proveedor
    }

    return render(request, 'core/proveedor/listar.html', data)



def modificar_proveedor(request, rut):

    proveedor = get_object_or_404(Proveedor, rut=rut)

    data = {
        'form': ProveedorForm(instance=proveedor)
    }

    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST, instance=proveedor, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Proveedor modificado exitosamente")
            return redirect(to="listar-proveedor")
        data["form"] = formulario    

    return render(request, 'core/proveedor/modificar.html', data)


def eliminar_proveedor(request, rut):
    proveedor = get_object_or_404(Proveedor, rut=rut)
    proveedor.delete()
    messages.success(request, "Proveedor eliminado exitosamente")
    return redirect(to="listar-proveedor")
