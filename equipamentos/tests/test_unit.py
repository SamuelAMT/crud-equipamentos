from django.test import TestCase
from ..models import Equipamento

class EquipamentoModelTest(TestCase):

    def test_create_equipamento(self):
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
        self.assertEqual(equipamento.nome, "Equipamento Teste")
        self.assertEqual(equipamento.tipo, "Tipo Teste")
        self.assertEqual(equipamento.fabricante, "Fabricante Teste")
        self.assertEqual(equipamento.modelo, "Modelo Teste")
        self.assertEqual(equipamento.numero_serie, "123456")
        self.assertEqual(equipamento.data_compra.strftime('%Y-%m-%d'), "2024-09-01")
        self.assertEqual(equipamento.valor_compra, 1000.00)
        self.assertEqual(equipamento.status, "Ativo")
        self.assertEqual(equipamento.data_ultima_manutencao.strftime('%Y-%m-%d'), "2024-08-01")
        self.assertEqual(equipamento.data_proxima_manutencao.strftime('%Y-%m-%d'), "2024-12-01")
        self.assertEqual(equipamento.descricao, "Descrição do equipamento de teste.")
