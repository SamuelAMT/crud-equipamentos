from django.db import models

class Equipamento(models.Model):
    tipo = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100, unique=True)
    data_compra = models.DateField()
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.tipo} - {self.fabricante} ({self.numero_serie})"
