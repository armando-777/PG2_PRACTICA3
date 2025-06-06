# Generated by Django 5.2 on 2025-06-05 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('localizacion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repuesto',
            old_name='direccion',
            new_name='modelo',
        ),
        migrations.RenameField(
            model_name='repuesto',
            old_name='telefono',
            new_name='precio',
        ),
        migrations.RemoveField(
            model_name='repuesto',
            name='email',
        ),
        migrations.RemoveField(
            model_name='repuesto',
            name='latitud',
        ),
        migrations.RemoveField(
            model_name='repuesto',
            name='longitud',
        ),
        migrations.AddField(
            model_name='experto',
            name='descripcion',
            field=models.TextField(default='Sin descripción'),
        ),
        migrations.AddField(
            model_name='repuesto',
            name='descripcion',
            field=models.TextField(default='Sin descripción'),
        ),
        migrations.AddField(
            model_name='taller',
            name='descripcion',
            field=models.TextField(default='Sin descripción'),
        ),
    ]
