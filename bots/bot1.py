"""main.py docstring"""

from datetime import datetime
from random import randint
import logging
import sys
import tweepy
import requests
sys.path.insert(0, '.')
import modules.credentials as credentials
import modules.actions as actions


logging.basicConfig(level=logging.INFO, filename='main.log',
                    filemode='w', format='bot0.py: %(levelname)s -> %(message)s')

# ? Constants declaration
CONSUMER_KEY = credentials.CONSUMER_KEY
CONSUMER_SECRET = credentials.CONSUMER_SECRET
ACCESS_TOKEN = credentials.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = credentials.ACCESS_TOKEN_SECRET
BEARER_TOKEN = credentials.BEARER_TOKEN
# Select location
WOEID = 766273  # 766273 = Madrid, Spain

# ? Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# ? Set up API
api = tweepy.API(auth)

# ? Set up Client
client = tweepy.Client(bearer_token=BEARER_TOKEN,
                       consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET,
                       return_type=requests.Response,
                       wait_on_rate_limit=True)


# ? Main decorator
def main_decorator(func):
    """ main() decorator docstring """

    def timer():
        """ main() wrapper docstring"""
        execution_time = datetime.now()
        print("\nExecuting bot0.py main()...\n")
        logging.info(f" Execution time: {execution_time}")
        func()
        print("\nFinished main() execution.\n")
        logging.info(f" Ending time: {datetime.now()}"), logging.info(
            f" Total execution time: {datetime.now() - execution_time}")
    return timer


@main_decorator
def main():
    """ main docstring """

    # ? Get last x tweets from a selected user
    # scrapped_tweets = actions.get_last_tweets(
    #     client, user='elonmusk', selection='retweet', count=10)
    # print(scrapped_tweets.text)

    # ? Post a tweet
    # twitter_post = actions.post_tweet(client, text='Hello, world!')
    # print(twitter_post)

    # Get the trends from the specified location (WOEID)
    trends = actions.get_trends(auth, WOEID)

    print(trends[0]['name'],
          trends[1]['name'],
          trends[2]['name'])

    # print(trends[0]['name'])
    # print(trends[0]['url'])
    # print(trends[0]['promoted_content'])
    # print(trends[0]['query'])
    # print(trends[0]['tweet_volume'])

    # ? Get the most popular tweets from a certain trend
    # actions.get_popular_tweets_hastag(api, f"{trends[0]['name']}", 1)

    # ? Get the most popular tweets from a certain user
    # actions.get_popular_tweets_user(api, f"from:elonmusk", 1)

    # ? Post a tweet for the most popular trend
    # reponses_list = ['Totalmente de acuerdo con ', 'No me lo puedo creer...',
                    #  'Vaya, vaya...', 'Quién lo iba a decir...', 'Qué vergüenza...',
                    #  '¡Madre mía!', '¡Esto es increible!', 'Pufgh...', 'No tiene sentido!!']

    # if trends[0]["name"][0] is "#":
        # trends[0]["name"] = trends[0]["name"][1:]
    # print(trends[0]["name"])

    # twitter_post = actions.post_tweet(
        # client, text=f'{reponses_list[randint(0, len(reponses_list)-1)]} #{trends[0]["name"]}')
    # print(twitter_post)

if __name__ == '__main__':
    main()
    