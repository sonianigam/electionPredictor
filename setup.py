import tweepy
import math
import cPickle as pickle
import pdb
import nltk
from nltk.tokenize import word_tokenize

consumer_key = "2j6vyRQ2DRerDGAQomcWfS8Ll"
secret_consumer_key = "28408qxsr8IzB0rghucxBDWqoOOvsbsYeIkJOJ3bQraVEsVKhC"

access_token = "497637135-krBrPRVaYlYm7FO0t4j8Ci6TzWkwlXab6E3vpEID"
secret_access_token = "RYuXPTCICXX0SgDMJ2Cu8GMkHVVAmBjYcUsRCDdYK5OSi"

auth = tweepy.OAuthHandler(consumer_key, secret_consumer_key)
auth.set_access_token(access_token, secret_access_token)

api = tweepy.API(auth)

accounts = {"hillary": ["HillaryClinton", "Beyonce", "kittukolluri", "Clanglotz"], "trump": ["realDonaldTrump", "peterthiel", "EdButowsky", "taylorjackson02", "ben_jammin002"], "bernie": ["BernieSanders", "Kaepernick7", "abzabec"]}

tweets = {"hillary": [], "trump": [], "bernie": []}

try:
    tweets = pickle.load(open("tweets.pickle", "rb"))
except (OSError, IOError) as e:
    for candidate in accounts:
        supporters = accounts[candidate]
        number = math.floor(1000/len(supporters))
        for user in supporters:
            user_tweets = api.user_timeline(user, count = number)
            tweets[candidate].extend([word_tokenize(t.text) for t in user_tweets])

    pickle.dump(tweets, open("tweets.pickle", "wb"))
