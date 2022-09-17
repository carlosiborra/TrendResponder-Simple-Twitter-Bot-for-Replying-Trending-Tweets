""" actions.py docstring """

import tweepy


tweet_list = []


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


def get_popular_tweets_hastag(api, selection='#yoursearch', num=5, return_type=None):
    """Get the last tweets from a hastag"""
    if return_type is None:
        for tweet in tweepy.Cursor(api.search_tweets, selection, result_type='popular').items(num):
            tweet_list.append(tweet)
        return tweet_list
    else:
        for tweet in tweepy.Cursor(api.search_tweets, selection, result_type='popular').items(num):
            tweet_list.append(tweet.id)
        return tweet_list


def get_popular_tweets_user(client, selection='from:elonmusk', num=5):
    """Get the last tweets from a user"""
    for tweet in tweepy.Cursor(client.search_tweets, selection, result_type='popular').items(num):
        tweet_list.append(tweet)
    return tweet_list


def get_user_metions(client, ids='1564736484321771520', num=5, start_time=None, end_time=None):
    """Get the last tweets from a user"""
    if not end_time and not start_time:
        mention = client.get_users_mentions(
            ids, max_results=num)
    elif not end_time:
        mention = client.get_user_metions(
            id=ids, max_results=num, start_time=start_time)
    else:
        mention = client.get_user_metions(
            id=ids, max_results=num, end_time=end_time, start_time=start_time)
    return mention


def post_tweet(client, text='Hello, world!', place_id="766273", in_reply_to_tweet_id=None):
    """Post a tweet"""
    if in_reply_to_tweet_id is None:
        tweet = client.create_tweet(text=text, place_id=place_id)
    else:
        tweet = client.create_tweet(
            text=text, place_id=place_id, in_reply_to_tweet_id=in_reply_to_tweet_id)
    return tweet
