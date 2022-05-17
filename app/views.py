from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request,'app/index.html')

#seccion listar
def perro(request):
    
    productoAll = Producto.objects.all() #llama a todos los productos

    datos = { #sirve para transportar los productos a la pagina
        'ListaProductos' : productoAll
    }

    if request.method == 'POST':
        carrito = Carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen_producto = request.POST.get('imagen_producto')
        carrito.save()

    return render(request,'app/perros.html', datos)

def gato(request):
    productoAll = Producto.objects.all() #llama a todos los productos

    datos = { #sirve para transportar los productos a la pagina
        'ListaProductos' : productoAll
    }
    if request.method == 'POST':
        carrito = Carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen_producto = request.POST.get('imagen_producto')
        carrito.save()
    return render(request,'app/gatos.html',datos)

def otros(request):
    productoAll = Producto.objects.all() #llama a todos los productos

    datos = { #sirve para transportar los productos a la pagina
        'ListaProductos' : productoAll
    }
    if request.method == 'POST':
        carrito = Carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen_producto = request.POST.get('imagen_producto')
        carrito.save()
    return render(request,'app/otros.html',datos)

def pago(request):
    carrito = Carrito.objects.all()
        
    carrito.delete()
    return render(request,'app/pago.html')
    

def carrito(request):
    carrito = Carrito.objects.all() #llama a todos los productos

    datos = { #sirve para transportar los productos a la pagina
        'ListaCarrito' : carrito
    }

    return render(request,'app/carrito.html', datos)

def historial(request):
    return render(request,'app/historial.html')

def index2(request):
    return render(request,'app/index_logueado.html')

def login(request):
    return render(request,'app/login.html')

def seguimiento(request):
    return render(request,'app/seguimiento.html')

def perfil(request):
    return render(request,'app/perfil.html')

def registrarse(request):
    return render(request,'app/registrarse.html')

def agregarProducto(request): #seccion agregar
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto Guardado Correctamente!"

    return render(request,'app/Productos/agregarProducto.html', datos)


def listar(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    
    return render(request, 'app/Productos/listar.html', datos)


def modificar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Producto modificado correctamente!'
            datos['form'] = formulario

    return render(request, 'app/Productos/modificar.html', datos)

def eliminar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listar")

def crud(request):
    return render(request,'app/crud.html')


def agregarCliente (request):

    datos = {
        'form' : ClienteForm()
    }
    if request.method == 'POST':
        formulario = ClienteForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Cliente Guardado Correctamente!"

    return render(request, 'app/cliente/agregarCliente.html',datos)


def listarCliente (request):

    productosAll = Cliente.objects.all()
    datos = {
        'listarCliente' : productosAll
    }
    
    return render(request,'app/cliente/listarCliente.html',datos)

def modificarCliente(request, codigo):
    cliente = Cliente.objects.get(codigo=codigo)
    datos = {
        'form' : ClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, files=request.FILES, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Cliente modificado correctamente!'
            datos['form'] = formulario
    return render(request, 'app/cliente/modificarCliente.html', datos)

def eliminarCliente(request, codigo):
    cliente = Cliente.objects.get(codigo=codigo)
    cliente.delete()
    return redirect(to="listarCliente")


