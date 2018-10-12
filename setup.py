import tweepy
import math
import pickle
import pdb
from nltk.tokenize.casual import TweetTokenizer
import config

auth = tweepy.OAuthHandler(config.consumer_key, config.secret_consumer_key)
auth.set_access_token(config.access_token, config.secret_access_token)
api = tweepy.API(auth)

accounts = {"democrat": ["HillaryClinton","kittukolluri", "Clanglotz", "stevendcoffey", "ezraklein", "ParkerMolloy", "TamikaDMallory" ], "republican": ["realDonaldTrump", "EdButowsky", "taylorjackson02", "ben_jammin002", "AppSame", "michellemalkin", "FredThompson"]}

tweets = {"democrat": [], "republican": []}

try:
    tweets = pickle.load(open("tweets.pickle", "rb"))
except (OSError, IOError) as e:
    tokenizer = TweetTokenizer(preserve_case=False, reduce_len=True)
    for party in accounts:
        supporters = accounts[party]
        number = math.floor(2000/len(supporters))
        for user in supporters:
            user_tweets = api.user_timeline(user, count = number)
            tweets[party].extend([tokenizer.tokenize(t.text.encode("utf-8")) for t in user_tweets])

    pickle.dump(tweets, open("tweets.pickle", "wb"))
