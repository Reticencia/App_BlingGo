from django.urls import path
from .views import ProductoGeneric

urlpatterns = [
    path('productos/', ProductoGeneric.as_view()),
]
