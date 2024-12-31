import tweepy
from config import (
    TWITTER_API_KEY,
    TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN,
    TWITTER_ACCESS_SECRET
)

def get_twitter_client():
    """Initialize and return Twitter API client"""
    client = tweepy.Client(
        consumer_key=TWITTER_API_KEY,
        consumer_secret=TWITTER_API_SECRET,
        access_token=TWITTER_ACCESS_TOKEN,
        access_token_secret=TWITTER_ACCESS_SECRET
    )
    return client

def get_trending_topics(client, woeid=1):
    """Get trending topics"""
    auth = tweepy.OAuth1UserHandler(
        TWITTER_API_KEY, 
        TWITTER_API_SECRET,
        TWITTER_ACCESS_TOKEN, 
        TWITTER_ACCESS_SECRET
    )
    api = tweepy.API(auth)
    trends = api.get_place_trends(woeid)
    return trends[0]["trends"]

def search_tweets(client, query, limit=10):
    """Search for tweets with engagement metrics"""
    tweets = client.search_recent_tweets(
        query=query,
        tweet_fields=['public_metrics', 'created_at'],
        max_results=limit
    )
    return tweets.data if tweets.data else [] 