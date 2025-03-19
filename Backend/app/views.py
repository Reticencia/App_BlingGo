from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response # Para la respuesta de la ubicacion
from rest_framework import status # Para alertar del estatus
from .models import usuarios
from .serializer import userSerializer
from geopy.distance import geodesic  # Para calcular distancia entre coordenadas


# Create your views here.

class UsuariosGeneric(generics.CreateAPIView):

    queryset = usuarios.objects.all()

    serializer_class = userSerializer

    # Agregue esta clase que compara las ubicaciones de el conductor y el uruario con geopy
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            ubicacion = serializer.save()

            # Si el usuario es un pasajero, buscar conductores cercanos
            if ubicacion.user_type == "usuario":
                conductores = Productos.objects.filter(user_type="conductor")

                for conductor in conductores:
                    distancia = geodesic(
                        (ubicacion.latitud, ubicacion.longitud),
                        (conductor.latitud, conductor.longitud)
                    ).meters  # Distancia en metros

                    if distancia <= 100:  # Si están a menos de 100 metros
                        return Response({"message": "¡El camión está cerca!"}, status=status.HTTP_200_OK)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


