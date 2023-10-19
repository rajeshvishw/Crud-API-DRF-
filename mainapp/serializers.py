from rest_framework import serializers
from .models import webModel
class webSerializer(serializers.ModelSerializer):
    class Meta:
        model = webModel
        fields = '__all__'