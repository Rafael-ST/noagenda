from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioSistema

class UsuarioSistemaForm(UserCreationForm):
    class Meta:
        model = UsuarioSistema
        fields = ["username", "email", "role", "consultorio", "password1", "password2"]
