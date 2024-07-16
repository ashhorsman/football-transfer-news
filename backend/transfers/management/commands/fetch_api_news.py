import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from transfers.models import TransferNews

class Command(BaseCommand):
    help = 'Fetch latest transfer news from third-party API'

    def handle(self, *args, **options):
        url = f'https://newsapi.org/v2/everything?q=football%20transfer&apiKey={settings.NEWS_API_KEY}'
        response = requests.get(url)

        if response.status_code == 200:
            news_data = response.json()
            for news_item in news_data['articles']:
                headline = news_item['title']
                content = news_item['description']
                published_at = news_item['publishedAt']

                TransferNews.objects.get_or_create(
                    headline=headline[:255],
                    content=content,
                    published_at=published_at
                )

            self.stdout.write(self.style.SUCCESS('Successfully fetched transfer news from API'))
        else:
            self.stderr.write(f'Failed to fetch transfer news from API. Status code: {response.status_code}')
            self.stderr.write(f'Response content: {response.content.decode()}')
