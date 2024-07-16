from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import TransferNews
from .serializers import TransferNewsSerializer

@api_view(['GET'])
def get_transfer_news(request):
    news = TransferNews.objects.all()
    serializer = TransferNewsSerializer(news, many=True)
    return Response(serializer.data)

def home_page(request):
    news = TransferNews.objects.all().order_by('-published_at')
    return render(request, 'home.html', {'news': news})