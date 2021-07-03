from django.urls import path
from .views import index, contacto, seccion_gatos, seccion_perros, formulario_enviado, agregar_proveedor, listar_proveedor, modificar_proveedor, eliminar_proveedor
from .views import contacto

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

]
