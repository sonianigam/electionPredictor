import setup
import nltk
import itertools
import string
import sys

def main():
    twitter_handle = input("Please enter your twitter handle: ")

    tweets = setup.tweets
    twitter_stopwords = ["rt", "#tcot", "’", "…", "“", "..."]
    punctuation = [c for c in string.punctuation]

    for party in tweets:
        print(party)
        content = itertools.chain.from_iterable(tweets[party])
        stopwords = nltk.corpus.stopwords.words('english') + punctuation + twitter_stopwords
        content = [word.lower() for word in content]
        filtered_content = [word for word in content if word not in stopwords]

        freq_dist = nltk.FreqDist(filtered_content)
        print(freq_dist.most_common(10))

def get_user_tweets(twitter_handle):
    auth = tweepy.OAuthHandler(config.consumer_key, config.secret_consumer_key)
    auth.set_access_token(config.access_token, config.secret_access_token)
    api = tweepy.API(auth)

if __name__ == "__main__":
    main()
