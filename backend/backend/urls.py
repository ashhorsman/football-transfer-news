from django.contrib import admin
from django.urls import path
from transfers.views import get_transfer_news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/news/', get_transfer_news),
]
