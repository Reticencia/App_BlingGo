from django.db import models

# Create your models here.

class Productos(models.Model):
    user_id = models.CharField(max_length=50)  # Identificación del usuario o conductor
    user_type = models.CharField(max_length=10)  # Puede ser "usuario" o "conductor"
    latitud = models.FloatField()
    longitud = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)


    
