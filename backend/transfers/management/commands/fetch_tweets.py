import tweepy
from django.core.management.base import BaseCommand
from django.conf import settings
from transfers.models import TransferNews

class Command(BaseCommand):
    help = 'Fetch latest transfer news tweets'

    def handle(self, *args, **options):
        auth = tweepy.OAuth1UserHandler(
            settings.TWITTER_API_KEY,
            settings.TWITTER_API_SECRET_KEY,
            settings.TWITTER_ACCESS_TOKEN,
            settings.TWITTER_ACCESS_TOKEN_SECRET
        )

        api = tweepy.API(auth)
        keywords = ["transfer", "football", "soccer", "rumor"]
        for keyword in keywords:
            tweets = api.search_tweets(q=keyword, count=10, lang="en")
            for tweet in tweets:
                TransferNews.objects.get_or_create(
                    headline=tweet.text[:255],
                    content=tweet.text,
                    published_at=tweet.created_at
                )
        self.stdout.write(self.style.SUCCESS('Successfully fetched tweets'))
