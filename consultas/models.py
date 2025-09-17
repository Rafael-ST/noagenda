from django.db import models
from app.static_data import STATUS_CONSULTA
from app.mixins import BaseModel
from pacientes.models import Paciente
from usuarios.models import UsuarioSistema


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(UsuarioSistema, limit_choices_to={'role': 'medico'}, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CONSULTA,  default="agendado")
    observacoes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
    
    def __str__(self):
        return f"{self.paciente} - {self.data_hora} / {self.medico}"
