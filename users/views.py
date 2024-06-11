from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Cliente, Turno
from .forms import ClienteForm, TurnoForm
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


def dashboard(request):
    turnos = Turno.objects.all()
    return render(request, 'users/dashboard.html', {
                'turnos': turnos,
                })
