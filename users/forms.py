from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Cliente, Turno, Producto, UsoProducto

class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn btn-primary'))

    class Meta:
        model = Cliente
        fields = ['nombre', 'telefono', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class TurnoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar', css_class='btn btn-primary'))

    class Meta:
        model = Turno
        fields = ['cliente', 'fecha', 'observacion', 'precio']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'observacion': forms.Select(choices=[('alisado', 'Alisado'), ('corte', 'Corte'), ('tintura', 'Tintura')], attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre', 'categoria', 'descripcion', 'fecha_vencimiento',
            'cantidad_disponible', 'precio_venta', 'compra', 'tipo',
            'adquisicion', 'marca', 'proveedor', 'notas', 'codigo_barras', 'imagen'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),  # Cambiado a TextInput
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
            'fecha_vencimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'cantidad_disponible': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control'}),
            'compra': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),  # Cambiado a TextInput
            'adquisicion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),  # Cambiado a DateInput
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'proveedor': forms.TextInput(attrs={'class': 'form-control'}),
            'notas': forms.Textarea(attrs={'class': 'form-control', 'rows': '4'}),
            'codigo_barras': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'nombre': 'Nombre del Producto',
            'categoria': 'Categoría',
            'descripcion': 'Descripción',
            'fecha_vencimiento': 'Fecha de Vencimiento',
            'cantidad_disponible': 'Cantidad Disponible',
            'precio_venta': 'Precio de Venta',
            'compra': 'Precio de Compra',
            'tipo': 'Unidad de Medida',
            'adquisicion': 'Fecha de adquisición',
            'marca': 'Marca',
            'proveedor': 'Proveedor',
            'notas': 'Notas',
            'codigo_barras': 'Código de Barras',
            'imagen': 'Imagen del Producto',
        }
        def clean(self):
            cleaned_data = super().clean()
            if cleaned_data.get('precio_venta') and cleaned_data.get('compra'):
                if cleaned_data['precio_venta'] <= cleaned_data['compra']:
                    raise forms.ValidationError("El precio de venta debe ser mayor que el precio de compra.")
            return cleaned_data
    

class UsoProductoForm(forms.ModelForm):
    producto = forms.ModelChoiceField(
        queryset=Producto.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    cantidad_usada = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = UsoProducto
        fields = ['producto', 'cantidad_usada']
    