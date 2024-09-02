from django.test import TestCase
from django.urls import reverse
from ..models import Equipamento

class EquipamentoIntegrationTest(TestCase):
    
    def test_equipamento_create_and_retrieve(self):
        equipamento = Equipamento.objects.create(
            nome="Equipamento Teste",
            tipo="Tipo Teste",
            fabricante="Fabricante Teste",
            modelo="Modelo Teste",
            numero_serie="123456",
            data_compra="2024-09-01",
            valor_compra="1000.00",
            status="Ativo",
            data_ultima_manutencao="2024-08-01",
            data_proxima_manutencao="2024-12-01",
            descricao="Descrição do equipamento de teste."
        )
        
        url = reverse('equipamento-detail', kwargs={'pk': equipamento.pk})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Equipamento Teste')
        self.assertContains(response, 'Tipo Teste')
        self.assertContains(response, 'Fabricante Teste')
        self.assertContains(response, 'Modelo Teste')
        self.assertContains(response, '123456')
        self.assertContains(response, '2024-09-01')
        self.assertContains(response, '1000.00')
        self.assertContains(response, 'Ativo')
        self.assertContains(response, '2024-08-01')
        self.assertContains(response, '2024-12-01')
        self.assertContains(response, 'Descrição do equipamento de teste.')
