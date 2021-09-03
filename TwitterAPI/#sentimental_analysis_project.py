#Importing Libraries
from typing import Text
from textblob import TextBlob
from tweepy import OAuthHandler
import tweepy
import sys 
import twitter


#Twitter Key
mykeys = open('TwitterK.txt', 'r').read().splitlines()
api_key = mykeys[0]
api_key_secret = mykeys[1]
access_token = mykeys[2]
access_token_secret = mykeys[3]
bearer_token = mykeys[4]

#Authentication
twitter_api = twitter.api(consumer_key=api_key, 
                        consumer_secret=api_key_secret,
                        access_token=access_token,
                        access_token_secret=access_token_secret)

print(twitter_api.VerifyCredential())

#Defining the Search Term
#search_term = 'Charlie Watts'

#Defining the Amount of Tweets max 500,000 per 24hs
#t_amount = 200
 
#Results
#tweets = tweepy.Cursor(api.search, q=search_term, lang='en').items(t_amount)

#Clearing the Data
#for tweet in tweets:
    #print(tweet)


