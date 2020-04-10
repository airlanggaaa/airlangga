import tweepy
import time
import random

print("Welcome")

CONSUMER_KEY = '2ufYDquie0Rm1eVdbQlUIp2xx'
CONSUMER_SECRET = 'rM6XRukHNMStaLqnTgHjuywJ9rMkKgKK4LoRCo30njToaikfMF'
ACCESS_KEY = '1248531637618364416-lbBsae2mawiLKTqBlUPFTH9i4YBl2u'
ACCESS_SECRET = 'wyCpCHzKx8GDKISgWhlfa4uHbuFrBukvtBr1f5fXPtzW5'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

with open('name.txt', 'r') as tweet_name:
    for name in tweet_name:
        tweet_hujat = random.choice(list(open('hujatan.txt')))
        tweet_seru = random.choice(list(open('seru.txt')))

        tweet = name[:-1] + tweet_hujat[:-1] + tweet_seru[:-1]
        print(tweet.upper())

tweet_name.close()