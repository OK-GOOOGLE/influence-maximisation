
from __future__ import unicode_literals
import tweepy
from tweepy import OAuthHandler
import json
from pymongo import MongoClient
import pymongo
import initReputation as alg

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
#
api = tweepy.API(auth)




# public_tweets = api.home_timeline(count=5)
# for tweet in public_tweets:
#     print(tweet.text)

# following = api.friends()

#
# inp_nickname = input("Provide screen name: ")
# print("searching for: " + inp_nickname + "...")

count = 1
# tweets = tweepy.Cursor(api.search, q="vote OR midterm OR midterms OR election OR democrats OR republicans OR Trump OR USA  Or America OR President OR November OR rally OR caucus OR presidential OR parties OR citizens OR reelection OR campaign OR advertisements",
#                            rpp=100, lang="en", tweet_mode="extended").items(10)

tweet = api.get_status(1065317920484585475)
print(tweet)
