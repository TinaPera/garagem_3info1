from django.db import models

from .cor import Cor
from .modelo import Modelo
from .acessorio import Acessorio

class Veiculo (models.Model):
    ano = models.IntegerField(default=0, null=True, blank=True)
    cor = models.ForeignKey(Cor, on_delete=models.RESTRICT)
    modelo = models.ForeignKey(Modelo, on_delete=models.RESTRICT)
    preco = models.DecimalField(decimal_places=2, max_digits=10, default=0, null=True, blank=True)
    acessorio = models.ManyToManyField(Acessorio)

    def __str__(self):
        return f'{self.modelo} - {self.ano} - {self.cor}'