from django.urls import path, include
from .views import index, contacto, seccion_gatos, seccion_perros, formulario_enviado, agregar_proveedor, listar_proveedor, modificar_proveedor, eliminar_proveedor, ProveedorViewset
from .views import contacto
from rest_framework import routers

router = routers.DefaultRouter()
router.register('proveedor', ProveedorViewset)

#localhost:8000/api/proveedor  carga la api GET Y POST AGREGA PROVEEDOR DE MANERA EXITOSA

urlpatterns = [

    path('', index, name="index"),
    path('contacto/', contacto, name="contacto"),
    path('seccion-gatos/', seccion_gatos, name="seccion-gatos"),
    path('seccion-perros/', seccion_perros, name="seccion-perros"),
    path('formulario-enviado/', formulario_enviado, name="formulario-enviado"),
    path('agregar-proveedor/', agregar_proveedor, name="agregar-proveedor"),
    path('listar-proveedor/', listar_proveedor, name="listar-proveedor"),
    path('modificar-proveedor/<rut>/', modificar_proveedor, name="modificar-proveedor"),
    path('eliminar-proveedor/<rut>/', eliminar_proveedor, name="eliminar-proveedor"),
    path('api/', include(router.urls)),

]
