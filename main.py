"""main.py docstring"""

import tweepy
import credentials
import requests

consumer_key = credentials.consumer_key
consumer_secret = credentials.consumer_secret
access_token = credentials.access_token
access_token_secret = credentials.access_token_secret
bearer_token = credentials.bearer_token

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Identifier of the place
WOEID = 766273

# Create a tweet
client = tweepy.Client(bearer_token=bearer_token,
                       consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret,
                       return_type=requests.Response,
                       wait_on_rate_limit=True)


# ? Get last 100 tweets from a selected user
# Define query
# query = 'from:elonmusk -is:retweet'

# Get max. 100 tweets
# tweets = client.search_recent_tweets(query=query,
# tweet_fields=['author_id', 'created_at'],
# max_results=100)

# print(tweets.text)

# ? Post a tweet
# response = client.create_tweet(text='hello world')
# print(response)

# ? Get the Tweeter trends at certain place (WOEID)
# Get the trends from an specific location
trends = tweepy.API(auth).get_place_trends(WOEID)

print(trends[0]['trends'][0]['name'],
      trends[0]['trends'][1]['name'],
      trends[0]['trends'][2]['name'])

print(trends[0]['trends'][0]['name'])
print(trends[0]['trends'][0]['url'])
print(trends[0]['trends'][0]['promoted_content'])
print(trends[0]['trends'][0]['query'])
print(trends[0]['trends'][0]['tweet_volume'])
