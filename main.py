# #
# from __future__ import unicode_literals
# import tweepy
# from tweepy import OAuthHandler
# import json
# from pymongo import MongoClient
# import pymongo
# import initReputation as rep
import ABC as abc
# #
# #
# consumer_key = '8KxiBh7H9xhUvjKfeBvjNHTGX'
# consumer_secret = 'WZHJOh7ZYEsNBsbbltruUMhMXsmurz9J3cTWHeDbeUSk9TLVuO'
# access_token = '805914750848794625-uhw7NpoR2G2tNJuvJXPSzPVZQG5UfTF'
# access_secret = '2S0sCT424c3ypIBYas4hU8wzPw5STaDLNPBuXVTkmuLeY'
#
# db = "db"
# Tweets = "Tweets"
#
# # auth = OAuthHandler(consumer_key, consumer_secret)
# # auth.set_access_token(access_token, access_secret)
# #
# # api = tweepy.API(auth)
#
# client = MongoClient('localhost', 27017)
# db = client[db]
# # Tweets = db[Tweets]
#
# Tweets = db[Tweets]
# # print(Tweets.find().count())
# # print()
#
#
#
# # following = api.friends()
#
#
# # inp_nickname = input("Provide screen name: ")
# # print("searching for: " + inp_nickname + "...")
#
# count = 1
# # tweets = tweepy.Cursor(api.search, q="vote OR midterm OR midterms OR election OR democrats OR republicans OR Trump OR USA  Or America OR President OR November OR rally OR caucus OR presidential OR parties OR citizens OR reelection OR campaign OR advertisements",
# #                            rpp=100, lang="en", tweet_mode="extended").items(10)
# # toFile = ''
# # for tweet in tweets:
# #     # print(tweet._json)
# #     post = Tweets.insert_one(tweet._json)
#     # print(post.inserted_id)
#
# # print(db.collection_names(include_system_collections=False))
#
# # print(Tweets.index_information())
# # print(Tweets.list_indexes())
#
#
#
#
# #
# # str = Tweets.list_indexes()
# # # for i  in str:
# # #     print(i)
# #
#
#
#
# # printing everything
# # for i in Tweets.find().limit(2):
# #     for j in i:
# #         print("\""+j+ "\": ", i[j], end=", ")
# #         print()
#
#
#
#
#
#
#
#
# users = {}
# for i in Tweets.find():
#         # print(i['user']['screen_name'], end=", ")
#         if 'retweeted_status' in i:
#             newRetUser = i['retweeted_status']['user']['screen_name']
#             users.setdefault(newRetUser,
#                              {"followers": i['retweeted_status']['user']['followers_count'],
#                               "following": i['retweeted_status']['user']['friends_count'],
#                               "tweets": 0,  # nie pobieramy z API zeby nie mieszac wplyw z innych dziedzin
#                               "retweets": 0,
#                               "retweetsSent": 0,
#                               "inft": 0.,
#                               "inf0": 0.,
#                               "rep": 0.0,
#                               "RetweetedBy" : []
#                               })
#         newUser = i['user']['screen_name']
#         users.setdefault(newUser,
#                          {"followers": i['user']['followers_count'],
#                           "following": i['user']['friends_count'],
#                           "tweets": 0,  # nie pobieramy z API zeby nie mieszac wplyw z innych dziedzin
#                           "retweets": 0,
#                           "retweetsSent": 0,
#                           "inft": 0.,
#                           "inf0": 0.,
#                           "rep": 0.0,
#                           "RetweetedBy": []
#                          })
#
#
#         # print()
# #
# rep.initInfluence(users)
# print('===END USERS PROCESSING===')
# # print(len(users))
# for i in Tweets.find():
#     if 'retweeted_status' in i:
#         rep.updateInfAndRetweet(users, i['retweeted_status']['user']['screen_name'],
#                                        i['user']['screen_name'])
#     else:
#         rep.updTweets(users[i['user']['screen_name']])
# #
# #
# #
# #
# for usr in users:
#     rep.updateReputation(users, usr)





#
#
#
# print('===END INF PROCESSING 1===')
#
# i = 0

#
# # for usr in users:
# #     print(users[usr])
# #     i += 1
# #     if i > 1000:
# #         break
#
#
# print(users['mflynnJR'])

import json
#
# f = open('usersjson2.txt', 'w+')
# f.write(json.dumps(users))

# f = open('usersjson2.txt', 'r')
# users = json.loads(f.read())
#
# print(users['BeeSaysPolitics']) # mflynnJR
# print(len(users))
#
# #
# print("\n \n")
# for i in abc.findTopKNodes():
#     print(i, end="\n")
# print("\n \n")