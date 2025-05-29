from django.shortcuts import render
# Python native imports
from datetime import timedelta

# External imports
from rest_framework import viewsets
from django.utils import timezone as tz

# Local imports
from localizacion.serializers import *
from localizacion.models import *


class LocalizacionuserViewSet(viewsets.ModelViewSet):
    queryset = Localizacionuser.objects.all()
    serializer_class = LocalizacionuserSerializer


class TallerViewSet(viewsets.ModelViewSet):
    queryset = Taller.objects.all()
    serializer_class = TallerSerializer
    
class ExpertoViewSet(viewsets.ModelViewSet):
    queryset = Experto.objects.all()
    serializer_class = ExpertoSerializer

class proveedorViewSet(viewsets.ModelViewSet):
    queryset = proveedor.objects.all()
    serializer_class = proveedorSerializer

class RepuestoViewSet(viewsets.ModelViewSet):
    queryset = Repuesto.objects.all()
    serializer_class = RepuestoSerializer

