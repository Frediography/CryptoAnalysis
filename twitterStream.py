#!/usr/bin/env python3
'''

This script:
Gets a stream of tweets, gets sentiment (& sentiment polarity)

'''

###################
# DEBUG ON OR OFF #
debug = 0 #########
# 1 = ON, 0 = OFF #
###################

from logins import ckey, csecret, atoken, asecret, mongodburl
import tweepy
from textblob import TextBlob
import dataset
import datetime
import json
import pymongo
from pymongo import MongoClient
import numpy as np

client = pymongo.MongoClient(mongodburl)
db = client.CryptoTrader

# Login to Twitter
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

# Create api variable to play with
api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        tweetdetails = {}
        now = datetime.datetime.now()
        text = status.text
        followers = status.user.followers_count
        blob = TextBlob(text)
        sent = blob.sentiment
        polarity = sent.polarity
        subjectivity = sent.subjectivity
        if sent != 0:
            if polarity != 0:
                tweetdetails['timeanddate'] = str(np.datetime64('now'))
                tweetdetails['tweet'] = str(text)
                tweetdetails['followercount'] = str(followers)
                tweetdetails['polarity'] = str(polarity)
                tweetdetails['subjectivity'] = str(subjectivity)
                if debug == 1:
                    print(tweetdetails)
                _id = db.tweets.insert(tweetdetails)
                print(_id)

    def on_error(self, status_code):
        if status_code == 420:
            return False

def main():
    eth_stream_listener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=eth_stream_listener)
    stream.filter(track=['ether', 'ethereum', '#eth', 'Vitalik Buterin'])

'''

### EXECUTE THE SCRIPT ###

'''

if __name__ == "__main__":
    main()
