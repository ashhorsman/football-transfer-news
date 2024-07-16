from rest_framework import generics, permissions, views
from rest_framework.response import Response
from django.db import models
from .models import TransferNews, Club, Player, Manager, FollowedClub, FollowedPlayer, FollowedManager
from .serializers import TransferNewsSerializer, ClubSerializer, PlayerSerializer, ManagerSerializer

class TransferNewsList(generics.ListAPIView):
    queryset = TransferNews.objects.all()
    serializer_class = TransferNewsSerializer

class ClubList(generics.ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class PlayerList(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class ManagerList(generics.ListAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class FollowClub(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        club_id = request.data.get('club_id')
        club = Club.objects.get(id=club_id)
        FollowedClub.objects.get_or_create(user=request.user, club=club)
        return Response({'status': 'Club followed'})

class UnfollowClub(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        club_id = request.data.get('club_id')
        club = Club.objects.get(id=club_id)
        FollowedClub.objects.filter(user=request.user, club=club).delete()
        return Response({'status': 'Club unfollowed'})

class FollowPlayer(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        player_id = request.data.get('player_id')
        player = Player.objects.get(id=player_id)
        FollowedPlayer.objects.get_or_create(user=request.user, player=player)
        return Response({'status': 'Player followed'})

class UnfollowPlayer(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        player_id = request.data.get('player_id')
        player = Player.objects.get(id=player_id)
        FollowedPlayer.objects.filter(user=request.user, player=player).delete()
        return Response({'status': 'Player unfollowed'})

class FollowManager(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        manager_id = request.data.get('manager_id')
        manager = Manager.objects.get(id=manager_id)
        FollowedManager.objects.get_or_create(user=request.user, manager=manager)
        return Response({'status': 'Manager followed'})

class UnfollowManager(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        manager_id = request.data.get('manager_id')
        manager = Manager.objects.get(id=manager_id)
        FollowedManager.objects.filter(user=request.user, manager=manager).delete()
        return Response({'status': 'Manager unfollowed'})

class GeneralFeed(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = request.user
        followed_clubs = FollowedClub.objects.filter(user=user).values_list('club_id', flat=True)
        followed_players = FollowedPlayer.objects.filter(user=user).values_list('player_id', flat=True)
        followed_managers = FollowedManager.objects.filter(user=user).values_list('manager_id', flat=True)
        
        queryset = TransferNews.objects.filter(
            models.Q(club_id__in=followed_clubs) |
            models.Q(player_id__in=followed_players) |
            models.Q(manager_id__in=followed_managers) |
            models.Q(is_general=True)
        ).distinct()
        
        serializer = TransferNewsSerializer(queryset, many=True)
        return Response(serializer.data)
