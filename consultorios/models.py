from django.db import models
from app.mixins import BaseModel


class Consultorio(BaseModel):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'Consultorio'
        verbose_name_plural = 'Consultorios'
    

    def __str__(self):
        return self.nome
