from django.test import TestCase
from django.urls import reverse
from ..models import Equipamento

class EquipamentoViewTest(TestCase):

    def setUp(self):
        self.equipamento = Equipamento.objects.create(
            nome='Equipamento 1',
            tipo='Tipo A',
            fabricante='Fabricante X',
            modelo='Modelo Y',
            numero_serie='123456',
            status='Ativo',
            valor_compra=1000.00
        )

    def test_equipamento_list_view(self):
        response = self.client.get(reverse('equipamento-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Equipamento 1')

    def test_equipamento_detail_view(self):
        response = self.client.get(reverse('equipamento-detail', kwargs={'pk': self.equipamento.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Equipamento 1')
