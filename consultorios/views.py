from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Consultorio
from django.urls import reverse_lazy


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "consultorio.html"
    login_url = "login"  # se não estiver logado, redireciona para login


class ConsultorioCreateView(LoginRequiredMixin, CreateView):
    model = Consultorio
    fields = ["nome", "endereco", "cnpj"]
    template_name = "consultorio_form.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        consultorio = form.save()
        # vincula ao usuário administrador que criou
        self.request.user.consultorio = consultorio
        self.request.user.save()
        return super().form_valid(form)
