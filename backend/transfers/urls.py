from django.urls import path
from . import views
from .api_views import TransferNewsList, FavoriteList, FavoriteDetail

urlpatterns = [
    path('', views.home_page, name='home'),
    path('api/news/', TransferNewsList.as_view(), name='transfer_news_list'),
    path('api/favorites/', FavoriteList.as_view(), name='favorite_list'),
    path('api/favorites/<int:pk>/', FavoriteDetail.as_view(), name='favorite_detail'),
]
