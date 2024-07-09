from django.db import models

from .categoria import Categoria
from .marca import Marca

class Modelo (models.Model):
    nome = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    marca = models.ForeignKey(Marca, on_delete=models.RESTRICT)
    
    def __str__(self):
        return f'{self.marca} - {self.nome}'