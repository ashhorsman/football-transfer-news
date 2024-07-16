from rest_framework import serializers
from .models import TransferNews, Favorite

class TransferNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferNews
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
