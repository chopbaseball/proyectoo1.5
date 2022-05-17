from importlib.resources import path
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('perros', perro, name="perro"),
    path('gatos', gato, name="gato"),
    path('otros', otros, name="otro"),
    path('pago', pago, name="pago"),
    path('carrito', carrito, name="carrito"),
    path('historial', historial, name="historial"),
    path('index_logueado', index2, name="index2"),
    path('login', login, name="login"),
    path('seguimiento', seguimiento, name="seguimiento"),
    path('crud', crud, name="crud"),
    path('perfil', perfil, name="perfil"),
    path('registrarse', registrarse, name="registrarse"),
    path('agregarProducto/', agregarProducto, name="agregarProducto"),
    path('modificar/<codigo>', modificar, name="modificar"),
    path('listar/', listar, name="listar"),
    path('eliminar/<codigo>', eliminar, name="eliminar"),
    path('agregarCliente/', agregarCliente, name="agregarCliente"),
    path('listarCliente/',listarCliente,name="listarCliente"),
    path('modificarCliente/<codigo>', modificarCliente, name="modificarCliente"),
    path('eliminarCliente/<codigo>', eliminarCliente, name="eliminarCliente"),
]


