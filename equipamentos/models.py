from django.db import models

class Equipamento(models.Model):
    STATUS_CHOICES = [
        ('em_uso', 'Em Uso'),
        ('em_estoque', 'Em Estoque'),
        ('manutencao', 'Em Manutenção'),
        ('nao_funcional', 'Não Funcional'),
    ]
    
    nome = models.CharField(max_length=255, blank=False, null=False, default='Equipamento sem nome')
    descricao = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='em_estoque')
    tipo = models.CharField(max_length=100, blank=False, null=False, default='Equipamento sem tipo')
    fabricante = models.CharField(max_length=100, blank=False, null=False, default='Fabricante desconhecido')
    modelo = models.CharField(max_length=100, blank=False, null=False, default='Modelo desconhecido')
    numero_serie = models.CharField(max_length=100, unique=True, blank=False, null=False, default='Número de série desconhecido')
    data_compra = models.DateField(blank=False, null=False, default='')
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
    data_ultima_manutencao = models.DateField(blank=True, null=True)
    data_proxima_manutencao = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.tipo} - {self.fabricante} ({self.numero_serie})"
