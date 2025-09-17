from django.db import models
from django.contrib.auth.models import AbstractUser
from app.static_data import ROLE_CHOICES
from app.mixins import BaseModel
from consultorios.models import Consultorio


class UsuarioSistema(AbstractUser, BaseModel):
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE, null=True, blank=True)
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="usuario_sistema_groups",
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="usuario_sistema_permissions",
        blank=True,
    )
