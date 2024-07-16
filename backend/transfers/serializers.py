from rest_framework import serializers
from .models import TransferNews

class TransferNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferNews
        fields = '__all__'
