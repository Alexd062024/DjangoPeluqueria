from django import forms
from .models import Cliente, Turno


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'email']

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['cliente', 'fecha', 'observacion']
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'observacion': forms.Select(choices=[('alisado', 'Alisado'), ('corte', 'Corte'), ('tintura', 'Tintura')]),
        }
