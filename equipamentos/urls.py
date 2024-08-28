from django.urls import path
from .views import EquipamentoListCreate, EquipamentoDetail

urlpatterns = [
    path('equipamentos/', EquipamentoListCreate.as_view(), name='equipamento-list-create'),
    path('equipamentos/<int:pk>/', EquipamentoDetail.as_view(), name='equipamento-detail'),
]
