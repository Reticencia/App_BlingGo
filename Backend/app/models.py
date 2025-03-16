from django.db import models

# Create your models here.

class Productos(models.Model):
    # Tipo de usuario
    USER_TYPES = [
        ('usuario', 'Usuario'),
        ('conductor', 'Conductor')
    ]

    user_id = models.CharField(max_length=100)  # Identificación del usuario o conductor
    user_type = models.CharField(max_length=10, choices=USER_TYPES)  # Usuario o Conductor
    latitud = models.FloatField()
    longitud = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

"""Instrucciones:
Copia y pega este codigo.
Ejecuta: python manage.py makemigrations ,en la terminal para que no tenga errores la base de datos.
Ejecuta: python manage.py migrate , tambien en la terminal para aplicar los cambios a la base de datos."""
    
