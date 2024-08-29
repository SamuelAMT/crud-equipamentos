from django.urls import path
from .views import EquipamentoListCreate, EquipamentoDetailUpdateDelete

urlpatterns = [
    path('equipamentos/', EquipamentoListCreate.as_view(), name='equipamento-list-create'),
    path('equipamentos/<int:pk>/', EquipamentoDetailUpdateDelete.as_view(), name='equipment-detail-update-delete'),
]
