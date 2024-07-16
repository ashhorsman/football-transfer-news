from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import TransferNews
from .serializers import TransferNewsSerializer

@api_view(['GET'])
def get_transfer_news(request):
    news = TransferNews.objects.all()
    serializer = TransferNewsSerializer(news, many=True)
    return Response(serializer.data)
