from rest_framework import serializers
from .models import usuarios

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = usuarios
        fields = '__all__'