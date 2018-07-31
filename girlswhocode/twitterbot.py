# Imports
import tweepy
import random
import time

# Keys and Access Tokens
CONSUMER_KEY    = 'NqW5KyhCVTB3jLdodq9kKvirS'
CONSUMER_SECRET = 'JeOTCpINdHLmZtYPT31KNluTVMzz7OFD2OFnXLZj57GVHL70p6'

ACCESS_TOKEN    = '1017154667120287744-HZe5RATdsdUqyT1yiwKUCUL5uChiPH'
ACCESS_SECRET   = 'JjcG5oHarPLabbBTGyYtNggU66swN9sf5Y3yNwQokWSSh'


tweets = ["don't forget that ", "perhaps they're real", "me duele la cara", "yo te quiero tal y como estas"]

# Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api  = tweepy.API(auth)

# Update Status
index = random.randint(0, len(tweets) -1)
api.update_status(tweets[index]) # randomly tweets
