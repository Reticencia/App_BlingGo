from django.shortcuts import render
from rest_framework import generics
from .models import Productos
from .serializer import ProductoSerializer

# Create your views here.

class ProductoGeneric(generics.CreateAPIView):

    queryset = Productos.objects.all()

    serializer_class = ProductoSerializer


