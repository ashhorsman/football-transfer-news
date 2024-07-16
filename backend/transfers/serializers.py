from rest_framework import serializers
from .models import TransferNews, Club, Player, Manager

class TransferNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferNews
        fields = '__all__'

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'
