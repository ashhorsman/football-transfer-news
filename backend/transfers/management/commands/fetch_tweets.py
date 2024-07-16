import tweepy
from django.core.management.base import BaseCommand
from django.conf import settings
from transfers.models import TransferNews

class Command(BaseCommand):
    help = 'Fetch latest transfer news tweets'

    def handle(self, *args, **options):
        # Authenticate to the Twitter API
        client = tweepy.Client(
            bearer_token=settings.TWITTER_BEARER_TOKEN
        )

        query = "transfer OR football OR soccer OR rumor -is:retweet lang:en"
        tweets = client.search_recent_tweets(query=query, tweet_fields=['created_at'], max_results=10)

        for tweet in tweets.data:
            TransferNews.objects.get_or_create(
                headline=tweet.text[:255],
                content=tweet.text,
                published_at=tweet.created_at
            )

        self.stdout.write(self.style.SUCCESS('Successfully fetched tweets'))
