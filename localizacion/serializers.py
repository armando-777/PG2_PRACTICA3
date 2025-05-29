from localizacion.models import *
from rest_framework import serializers


class LocalizacionuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacionuser
        fields = [
            "id",
            "nombre",
            "latitud",
            "longitud",
           
        ]

class TallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taller
        fields = "__all__"

class ExpertoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experto
        fields = "__all__"
class proveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = proveedor
        fields = "__all__"
class RepuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repuesto
        fields = "__all__"
