from rest_framework import serializers
from .models import Aerolinea, Vuelo

class AerolineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aerolinea
        fields = ["codigo", "nombre"]

class VueloSerializer(serializers.ModelSerializer):
    aerolinea_nombre = serializers.CharField(source="aerolinea.nombre", read_only=True)

    class Meta:
        model = Vuelo
        fields = ["codigo", "destino", "duracion_minutos", "precio", "activo", "aerolinea"]

        #                                                                                    ^^^^^^^^^^^^^^^^
        #                                                                                    Este faltaba