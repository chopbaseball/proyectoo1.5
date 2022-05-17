
from django.contrib import admin

from app.views import carrito
from .models import *


# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display=['codigo','nombre','descripcion','precio','stock','tipo','imagen']
    search_fields = ['codigo']

class comuna(admin.ModelAdmin):
    list_display=['codigo','comuna']
    search_fields = ['codigo']

class cliente(admin.ModelAdmin):
    list_display=['codigo','nombre','apellido','rut','correo','numero','direccion','comuna']
    search_fields = ['codigo']

class CarritoAdmin(admin.ModelAdmin):
    list_display=['id','nombre_producto','precio_producto','imagen_producto']
    search_fields = ['id']



admin.site.register(TipoProducto)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Comuna)
admin.site.register(Cliente)
admin.site.register(Carrito, CarritoAdmin)
