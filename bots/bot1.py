"""bot0.py docstring"""

from datetime import datetime
from random import randint
import logging
import sys
sys.path.insert(0, '.')
import modules.actions as actions
import modules.config as config


api, client, auth = config.set_up_api()

# ? Main decorator
def main_decorator(func):
    """ main() decorator docstring """

    def timer():
        """ main() wrapper docstring"""
        execution_time = datetime.now()
        print("\nExecuting bot1.py main()...\n")
        logging.info(f"Executing bot1.py main()..."), logging.info(
            f"Execution time: {execution_time}")
        func()
        print("\nFinished bot1.py main() execution.\n")
        logging.info(f"Ending time: {datetime.now()}"), logging.info(
            f"Total execution time: {datetime.now() - execution_time}")
    return timer


@main_decorator
def main():
    """ main docstring """

    # ? Select location
    woeid = 766273  # 766273 = Madrid, Spain

    # ? Get last x tweets from a selected user
    # scrapped_tweets = actions.get_last_tweets(
    #     client, user='elonmusk', selection='retweet', count=10)
    # print(scrapped_tweets.text)

    # ? Post a tweet
    # twitter_post = actions.post_tweet(client, text='Hello, world!')
    # print(twitter_post)

    # Get the trends from the specified location (woeid)
    trends = actions.get_trends(auth, woeid)

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
    