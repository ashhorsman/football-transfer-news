from rest_framework import generics, filters
from .models import TransferNews, Favorite
from .serializers import TransferNewsSerializer, FavoriteSerializer
from rest_framework.permissions import IsAuthenticated

class TransferNewsList(generics.ListAPIView):
    queryset = TransferNews.objects.all().order_by('-published_at')
    serializer_class = TransferNewsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['headline', 'content']

class FavoriteList(generics.ListCreateAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FavoriteDetail(generics.RetrieveDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]
