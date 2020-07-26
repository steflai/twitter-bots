import tweepy
from textblob import TextBlob
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler (consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# search for tweets
positive_tweets = 0
negative_tweets = 0
neutral_tweets = 0

for tweet in tweepy.Cursor(api.search, q='milk').items(1000):
    # print (tweet.text)
    analysis = TextBlob(tweet.text)
    # print (analysis.sentiment)
    if analysis.sentiment[0]>0:
        # print ("Positive")
        positive_tweets = positive_tweets + 1
    elif analysis.sentiment[0]<0:
        # print ("Negative")
        negative_tweets = negative_tweets + 1
    else:
        # print ("Neutral")
        neutral_tweets = neutral_tweets + 1

api.update_status(status ="Today, MilkBot found {} positive, {} negative and {} neutral tweets about milk out of 1000 tweets".format(positive_tweets, negative_tweets, neutral_tweets))

if positive_tweets > negative_tweets:
    api.update_status(status = "The interent is feeling good about milk today")
