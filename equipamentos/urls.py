from django.urls import path
from .views import EquipamentoListCreate, EquipamentoDetailUpdateDelete, index

urlpatterns = [
    path('', index, name='index'),
    path('equipamentos/', EquipamentoListCreate.as_view(), name='equipamento-list-create'),
    path('equipamentos/<int:pk>/', EquipamentoDetailUpdateDelete.as_view(), name='equipamento-detail-update-delete'),
]
