from rest_framework import serializers
from .models import TransferNews, Club, Player, Manager, FollowedClub, FollowedPlayer, FollowedManager

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

class FollowedClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowedClub
        fields = '__all__'

class FollowedPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowedPlayer
        fields = '__all__'

class FollowedManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowedManager
        fields = '__all__'
