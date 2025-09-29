from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "consultorio.html"
    login_url = "login"  # se não estiver logado, redireciona para login
