from rest_framework import serializers
from .models import Equipamento

class EquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipamento
        fields = '__all__'
        extra_kwargs = {
            'nome': {'required': True},
            'tipo': {'required': True},
            'fabricante': {'required': True},
            'modelo': {'required': True},
            'numero_serie': {'required': True},
        }
