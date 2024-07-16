from django.urls import path
from . import api_views

urlpatterns = [
    path('news/', api_views.TransferNewsList.as_view(), name='transfer-news-list'),
    path('clubs/', api_views.ClubList.as_view(), name='club-list'),
    path('players/', api_views.PlayerList.as_view(), name='player-list'),
    path('managers/', api_views.ManagerList.as_view(), name='manager-list'),
    path('follow/club/', api_views.FollowClub.as_view(), name='follow-club'),
    path('unfollow/club/', api_views.UnfollowClub.as_view(), name='unfollow-club'),
    path('follow/player/', api_views.FollowPlayer.as_view(), name='follow-player'),
    path('unfollow/player/', api_views.UnfollowPlayer.as_view(), name='unfollow-player'),
    path('follow/manager/', api_views.FollowManager.as_view(), name='follow-manager'),
    path('unfollow/manager/', api_views.UnfollowManager.as_view(), name='unfollow-manager'),
    path('feed/', api_views.GeneralFeed.as_view(), name='general-feed'),
]
