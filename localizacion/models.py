from django.db import models

# Create your models here.

class Localizacionuser(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()

class Taller(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    localizaciones = models.ManyToManyField(Localizacionuser) # Relación Muchos a Muchos con Localizacion

class Experto(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    talleres = models.ManyToManyField(Taller) # Relación Muchos a Muchos con Taller

class proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    talleres = models.ManyToManyField(Taller) # Relación Muchos a Muchos con Taller
    repuestos = models.ManyToManyField('Repuesto') # Relación Muchos a Muchos con Repuesto

class Repuesto(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    proveedores = models.ManyToManyField(proveedor) # Relación Muchos a Muchos con Distribuidor

   

    
    


