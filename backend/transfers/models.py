from django.db import models
from django.contrib.auth.models import User

class TransferNews(models.Model):
    headline = models.CharField(max_length=255)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news_item = models.ForeignKey(TransferNews, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
