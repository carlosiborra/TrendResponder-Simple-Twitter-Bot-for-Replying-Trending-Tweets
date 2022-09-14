""" actions.py docstring """

import tweepy


def get_trends(auth, woeid=766273):
    """Get the trends from an specific location given a WOEID"""
    trends = tweepy.API(auth).get_place_trends(woeid)
    return trends[0]['trends']


def get_last_tweets(client, user='elonmusk', selection='retweet', count=100):
    """Get the last tweets from a user"""
    query = f'from:{user} -is:{selection}'
    tweets = client.search_recent_tweets(query=query, tweet_fields=[
                                         'author_id', 'created_at'], max_results=count)
    return tweets


def post_tweet(client, text='Hello, world!'):
    """Post a tweet"""
    tweet = client.create_tweet(text=text)
    return tweet

def get_popular_tweets_hastag(api, selection='#yoursearch', num=5):
    """Get the last tweets from a user"""
    for tweet in tweepy.Cursor(api.search_tweets, selection, result_type='popular').items(num):
        print(tweet)

# def get_popular_tweets_user(client, selection='from:elonmusk', selection='retweet', count=100):
#     """Get the last tweets from a user"""
#     for tweet in tweepy.Cursor(client.search, q='#yoursearch',result_type='popular').items(5):
#         print(tweet)
#     return tweets
