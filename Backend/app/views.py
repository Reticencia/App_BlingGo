from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Productos
from .serializer import ProductoSerializer# RegisterSerializer  # Importamos el serializador de registro

# Crear Producto
class ProductoGeneric(generics.CreateAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductoSerializer
    #permission_classes = [permissions.IsAuthenticated]

# Actualizar Ubicación
class updateLocation(generics.UpdateAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductoSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return Productos.objects.first()

# Registrar Usuario - Estudar esto
"""
class RegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]  # Permitir que cualquier usuario se registre
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Usuario registrado con éxito"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""