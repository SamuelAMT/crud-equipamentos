from django.test import TestCase
from ..models import Equipamento

class EquipamentoModelTest(TestCase):

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

    def test_equipamento_creation(self):
        self.assertIsInstance(self.equipamento, Equipamento)
        self.assertEqual(self.equipamento.nome, 'Equipamento 1')
        self.assertEqual(self.equipamento.tipo, 'Tipo A')
        self.assertEqual(self.equipamento.fabricante, 'Fabricante X')

    def test_equipamento_str_representation(self):
        self.assertEqual(str(self.equipamento), 'Equipamento 1')