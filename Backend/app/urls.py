from django.urls import path
from .views import UsuariosGeneric

urlpatterns = [
    path('productos/', UsuariosGeneric.as_view()),
]
