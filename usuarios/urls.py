from django.urls import path
from .views import UsuarioCreateView, LoginView, LogoutView


urlpatterns = [
    path("registrar/", UsuarioCreateView.as_view(), name="registrar"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
