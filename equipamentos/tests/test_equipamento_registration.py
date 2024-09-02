from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from ..models import Equipamento

class EquipamentoAPITest(APITestCase):
    
    def setUp(self):
        self.equipamento_data = {
            "nome": "Equipamento Teste",
            "tipo": "Tipo Teste",
            "fabricante": "Fabricante Teste",
            "modelo": "Modelo Teste",
            "numero_serie": "123456",
            "data_compra": "2024-09-01",
            "valor_compra": "1000.00",
            "status": "Ativo",
            "data_ultima_manutencao": "2024-08-01",
            "data_proxima_manutencao": "2024-12-01",
            "descricao": "Descrição do equipamento de teste."
        }

    def test_create_equipamento(self):
        url = reverse('equipamento-create')
        response = self.client.post(url, self.equipamento_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Equipamento.objects.count(), 1)
        self.assertEqual(Equipamento.objects.get().nome, 'Equipamento Teste')

    def test_get_equipamento_list(self):
        Equipamento.objects.create(**self.equipamento_data)
        url = reverse('equipamento-list')
        response = self.client.get(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nome'], 'Equipamento Teste')

    def test_update_equipamento(self):
        equipamento = Equipamento.objects.create(**self.equipamento_data)
        url = reverse('equipamento-detail', kwargs={'pk': equipamento.pk})
        updated_data = self.equipamento_data.copy()
        updated_data['nome'] = 'Equipamento Updated'
        
        response = self.client.put(url, updated_data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        equipamento.refresh_from_db()
        self.assertEqual(equipamento.nome, 'Equipamento Updated')

    def test_delete_equipamento(self):
        equipamento = Equipamento.objects.create(**self.equipamento_data)
        url = reverse('equipamento-detail', kwargs={'pk': equipamento.pk})
        
        response = self.client.delete(url, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Equipamento.objects.count(), 0)
