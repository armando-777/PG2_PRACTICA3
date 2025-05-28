from localizacion.models import *
from rest_framework import serializers


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacionuser
        fields = [
            "id",
            "nombre",
            "latitud",
            "longitud",
           
        ]

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taller
        fields = "__all__"

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experto
        fields = "__all__"
class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = proveedor
        fields = "__all__"
class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repuesto
        fields = "__all__"
