import feedparser
from django.core.management.base import BaseCommand
from transfers.models import TransferNews

class Command(BaseCommand):
    help = 'Fetch latest transfer news from RSS feed'

    def handle(self, *args, **options):
        url = 'https://www.goal.com/en/feeds/news?fmt=rss'  # Example RSS feed URL
        feed = feedparser.parse(url)

        for entry in feed.entries:
            headline = entry.title
            content = entry.summary
            published_at = entry.published

            TransferNews.objects.get_or_create(
                headline=headline[:255],
                content=content,
                published_at=published_at
            )

        self.stdout.write(self.style.SUCCESS('Successfully fetched transfer news from RSS feed'))
