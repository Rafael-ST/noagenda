from django.urls import path
from .views import UsuarioCreateView, LoginView, LogoutView, MedicosListView, SecretariasListView


urlpatterns = [
    path("registrar/", UsuarioCreateView.as_view(), name="registrar"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("medicos/", MedicosListView.as_view(), name="medicos_list"),
    path("secretarias/", SecretariasListView.as_view(), name="secretarias_list"),
]
