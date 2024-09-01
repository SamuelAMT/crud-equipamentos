from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Equipamento

class EquipamentoAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.equipamento_data = {
            "nome": "Equipamento Teste",
            "descricao": "Descrição do equipamento teste",
            "status": "Em Estoque",
            "tipo": "Tipo Teste",
            "fabricante": "Fabricante Teste",
            "modelo": "Modelo Teste",
            "numero_serie": "1234567890",
            "data_compra": "2024-08-31",
            "valor_compra": "1000.00"
        }
        self.url = reverse('equipamento-list-create')

    def test_create_equipamento_success(self):
        response = self.client.post(self.url, self.equipamento_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Equipamento.objects.count(), 1)

    def test_create_equipamento_missing_fields(self):
        invalid_data = self.equipamento_data.copy()
        invalid_data.pop('nome')
        response = self.client.post(self.url, invalid_data, format='json')
        self.assertEqual(response.status_code, 400)
