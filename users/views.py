from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Cliente, Turno, Producto
from .forms import ClienteForm, TurnoForm, ProductoForm
from django.contrib import messages


@login_required
def turnos(request):
    if request.method == 'POST':
        turno_form = TurnoForm(request.POST)
        if turno_form.is_valid():
            turno_form.save()
            return redirect('turnos')
    else:
        turno_form = TurnoForm()
    
    turnos = Turno.objects.all()
    return render(request, 'users/turnos.html', {
        'turno_form': turno_form,
    })

@login_required
def registro(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('registro')
    else:
        cliente_form = ClienteForm()
    
    return render(request, 'users/registrar.html', {
        'cliente_form': cliente_form,
    })

def home(request):
    return render(request, 'users/home.html')


def inventario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inventario')
    else:
        form = ProductoForm()
        
    productos = Producto.objects.all()
    print(productos)
    return render(request, 'users/inventario.html', {'productos': productos, 'form': form})


def dashboard(request):
    turnos = Turno.objects.all()
    return render(request, 'users/dashboard.html', {
                'turnos': turnos,
                })


def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('inventario')
    return render(request, 'users/inventario.html', {'eliminar_producto': producto})

