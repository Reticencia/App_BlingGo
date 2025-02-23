from django.db import models

# Create your models here.

class Productos(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)


    
