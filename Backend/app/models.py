from django.db import models
#from django.contrib.auth.models import User

# Create your models here.

class Productos(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el usuario
    latitud = models.FloatField()
    longitud = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)


