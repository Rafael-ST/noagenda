from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from .models import UsuarioSistema
from .forms import UsuarioSistemaForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class UsuarioCreateView(CreateView):
    model = UsuarioSistema
    form_class = UsuarioSistemaForm
    template_name = "registrar.html"
    success_url = reverse_lazy("login")  # redireciona para login depois de registrar


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
            return redirect("home")  # ajuste para onde o usuário deve ir após login
        else:
            messages.error(request, "Usuário ou senha inválidos.")
            return render(request, self.template_name)


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Você saiu da sua conta.")
        return redirect("login")  # redireciona para a tela de login
