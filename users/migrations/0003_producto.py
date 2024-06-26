# Generated by Django 4.2.2 on 2024-06-25 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_turno_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('categoria', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('fecha_vencimiento', models.DateField()),
                ('cantidad_disponible', models.IntegerField()),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('compra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo', models.CharField(max_length=255)),
                ('adquisicion', models.CharField(max_length=255)),
                ('marca', models.CharField(max_length=255)),
                ('proveedor', models.CharField(max_length=255)),
                ('notas', models.TextField(blank=True, null=True)),
                ('codigo_barras', models.CharField(max_length=255)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos/')),
            ],
        ),
    ]
