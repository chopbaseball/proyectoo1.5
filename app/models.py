from re import T
from django.db import models

# Create your models here.

class TipoProducto(models.Model):
    tipo_productos = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo_productos
    
    class Meta:
        db_table = 'db_tipo_producto'

class Producto(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=40)
    precio = models.IntegerField()
    stock = models.IntegerField()
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    create_at = models.DateField(auto_now_add=True) #guarda producto con la fecha actual
    update_at = models.DateField(auto_now=True)

    #para separar las imagenes se cambia el nombre en upload to

    def __str__(self):
        return self.nombre
    
    class Meta:
        db_table = 'db_producto'

class Carrito(models.Model):
    nombre_producto = models.CharField(max_length=20)
    precio_producto = models.IntegerField()
    imagen_producto = models.ImageField(upload_to ="Carrito", null= True)

    def __str__(self):
        return self.nombre_producto
    
    class Meta:
        db_table = 'db_Carrito'

class Comuna(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    comuna = models.CharField(max_length=25)
    def __str__(self):
        return self.comuna
    
    class Meta:
        db_table = 'db_comuna'

class Cliente(models.Model):
    codigo = models.IntegerField(null=False, primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    rut = models.CharField(max_length=13)
    correo = models.CharField(max_length=30)
    numero = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table = 'db_cliente'
