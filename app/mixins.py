# app/mixins.py

import uuid
from django.db import models
from django.utils.timezone import now


# 🆔 UUID primário
class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


# 🕒 Timestamps automáticos
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        abstract = True


# ✅ Ativo/Inativo
class AtivoInativoModel(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='Ativo')

    class Meta:
        abstract = True


# 🎯 BaseModel flexível
class BaseModel(UUIDModel, TimeStampedModel):
    # Manager padrão que ignora soft delete
    objects = models.Manager()

    class Meta:
        abstract = True
