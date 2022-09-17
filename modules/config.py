""" config.py docstring """

import logging
import tweepy
import requests
from modules import credentials

def  set_up_api():
    """ set_up_api() docstring """

    logging.basicConfig(level=logging.INFO, filename='main.log',
                    filemode='w', format='%(levelname)s -> %(message)s', force=True)

    # ? Constants declaration
    CONSUMER_KEY = credentials.CONSUMER_KEY
    CONSUMER_SECRET = credentials.CONSUMER_SECRET
    ACCESS_TOKEN = credentials.ACCESS_TOKEN
    ACCESS_TOKEN_SECRET = credentials.ACCESS_TOKEN_SECRET
    BEARER_TOKEN = credentials.BEARER_TOKEN

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

    return api, client, auth
