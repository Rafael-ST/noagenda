from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, View, ListView
from .models import UsuarioSistema
from .forms import UsuarioSistemaForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class UsuarioCreateView(CreateView):
    model = UsuarioSistema
    form_class = UsuarioSistemaForm
    template_name = "registrar.html"
    success_url = reverse_lazy("login")


class LoginView(View):
    template_name = "login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect("home")
        else:
            messages.error(request, "Usuário ou senha inválidos.")
            return render(request, self.template_name)


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Você saiu da sua conta.")
        return redirect("login")


class MedicosListView(LoginRequiredMixin, ListView):
    model = UsuarioSistema
    template_name = "medicos_list.html"
    context_object_name = "medicos"

    def get_queryset(self):
        return UsuarioSistema.objects.filter(role="medico", consultorio=self.request.user.consultorio)


class SecretariasListView(LoginRequiredMixin, ListView):
    model = UsuarioSistema
    template_name = "secretarias_list.html"
    context_object_name = "secretarias"

    def get_queryset(self):
        return UsuarioSistema.objects.filter(role="secretaria", consultorio=self.request.user.consultorio)
