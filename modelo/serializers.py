from rest_framework import serializers
from .models import CalculoModelo, UnidadHidrologica, DatosGeneradosUnidad

class UnidadHidrologicaSerializer(serializers.ModelSerializer):

    class Meta:
        model = UnidadHidrologica
        fields = ('__all__')

class CalculoModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculoModelo
        fields = ('__all__')

class DatosGeneradosUnidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosGeneradosUnidad
        fields = ('__all__') 

       
