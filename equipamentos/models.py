from django.db import models

class Equipamento(models.Model):
    STATUS_CHOICES = [
        ('Em Uso', 'Em Uso'),
        ('Em Estoque', 'Em Estoque'),
        ('Manutenção', 'Em Manutenção'),
        ('Não Funcional', 'Não Funcional'),
    ]
    
    nome = models.CharField(max_length=255, blank=False, null=False, default='Equipamento sem nome')
    tipo = models.CharField(max_length=100, blank=False, null=False, default='Equipamento sem tipo')
    fabricante = models.CharField(max_length=100, blank=False, null=False, default='Fabricante desconhecido')
    modelo = models.CharField(max_length=100, blank=False, null=False, default='Modelo desconhecido')
    numero_serie = models.CharField(max_length=100, unique=True, blank=False, null=False, default='Número de série desconhecido')
    data_compra = models.DateField(blank=False, null=False, default='')
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Em Estoque')
    data_ultima_manutencao = models.DateField(blank=True, null=True)
    data_proxima_manutencao = models.DateField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.tipo} - {self.fabricante} ({self.numero_serie})"
