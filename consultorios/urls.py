from django.urls import path
from .views import HomeView, ConsultorioCreateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("consultorio/novo/", ConsultorioCreateView.as_view(), name="criar_consultorio"),
]
