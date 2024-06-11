from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Cliente, Turno
from .forms import ClienteForm, TurnoForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        turno_form = TurnoForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('profile')
        if turno_form.is_valid():
            turno_form.save()
            return redirect('profile')
    else:
        cliente_form = ClienteForm()
        turno_form = TurnoForm()
    
    turnos = Turno.objects.all()
    return render(request, 'users/profile.html', {
        'cliente_form': cliente_form,
        'turno_form': turno_form,
        'turnos': turnos
    })


def home(request):
    return render(request, 'users/home.html')
