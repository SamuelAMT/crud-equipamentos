from rest_framework import generics
from .models import Equipamento
from .serializers import EquipamentoSerializer

class EquipamentoListCreate(generics.ListCreateAPIView):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer

class EquipamentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipamento.objects.all()
    serializer_class = EquipamentoSerializer
