# Generated by Django 4.2.2 on 2024-06-28 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='adquisicion',
            field=models.DateField(),
        ),
    ]
