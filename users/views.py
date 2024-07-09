from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Cliente, Turno, Producto, UsoProducto
from .forms import ClienteForm, TurnoForm, ProductoForm, UsoProductoForm
from django.contrib import messages
from django.db import transaction
from django.http import JsonResponse
from datetime import timedelta
from django.utils import timezone


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
            try:
                producto = form.save()
                messages.success(request, f'Producto "{producto.nombre}" creado exitosamente.')
                return redirect('inventario')
            except Exception as e:
                messages.error(request, f'Error al guardar el producto: {str(e)}')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = ProductoForm()
        
    productos = Producto.objects.all()
    uso_form = UsoProductoForm()
    return render(request, 'users/inventario.html', {'productos': productos, 'form': form, 'uso_form': uso_form})


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


@login_required
@transaction.atomic
def registrar_uso_producto(request):
    if request.method == 'POST':
        uso_form = UsoProductoForm(request.POST)
        if uso_form.is_valid():
            uso_producto = uso_form.save(commit=False)
            producto = uso_producto.producto
            cantidad_usada = uso_producto.cantidad_usada

            if cantidad_usada > producto.cantidad_disponible:
                return JsonResponse({'success': False, 'error': 'La cantidad usada no puede ser mayor que la cantidad disponible.'})
            else:
                producto.cantidad_disponible -= cantidad_usada
                producto.save()
                uso_producto.save()
                return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Por favor, corrija los errores en el formulario.'})
    else:
        return JsonResponse({'success': False, 'error': 'Método no permitido.'})
    

def historial_uso(request):
    fecha_inicio = timezone.now() - timedelta(days=30)
    fecha_fin = timezone.now()

    if request.GET.get('fecha_inicio'):
        fecha_inicio = timezone.datetime.strptime(request.GET['fecha_inicio'], '%Y-%m-%d')
    if request.GET.get('fecha_fin'):
        fecha_fin = timezone.datetime.strptime(request.GET['fecha_fin'], '%Y-%m-%d')

    fecha_fin = fecha_fin.replace(hour=23, minute=59, second=59, microsecond=999999)

    usos = UsoProducto.objects.filter(fecha_uso__range=(fecha_inicio, fecha_fin))

    context = {
        'usos': usos,
        'fecha_inicio': fecha_inicio.strftime('%Y-%m-%d'),
        'fecha_fin': fecha_fin.strftime('%Y-%m-%d'),
    }
    return render(request, 'users/historial_uso.html', context)