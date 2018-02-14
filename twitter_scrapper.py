import tweepy
import csv
import pandas as pd


####input your credentials here
consumer_key = 'FUCgrYe39KQsaTVxPaOqvdqak'
consumer_secret = 'GquA7RKS3AfLyaStE9Lcvx7ukFSSAzNfELY3eRgsYlsd7G9jgB'
access_token = '1097111352-SempPyR4D5LhWLYj0VtQNHNBtx6jDDyugIBgrIF'
access_secret = 'EzkffPwHypdRTwAHiwhoObJI2XwWWg6q3tOdhsEeCDZpA'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#==========| If we want to safe to file on RUN |=============

# Open/Create a file to append data
#csvFile = open('twitter.csv', 'a')

#Use csv Writer
#csvWriter = csv.writer(csvFile)

									 #SEARH TERM#
for tweet in tweepy.Cursor(api.search,q="#420",count=100, 
                           lang="en",
                           since="2018-02-12").items():
    print (tweet.created_at, tweet.text)
    #csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

#geolocations
#GEOBOX_WORLD = [-180,-90,180,90]
#stream.filter(locations=GEOBOX_WORLD)