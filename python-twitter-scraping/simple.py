import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob

# import twitter keys and tokens
from config import *

class TweetStreamListener(StreamListener):

	#on success
	def on_data(self,data):

		# output raw data
		print(data)

		return True
	#on failure

	def on_error(self,status):
		print (status)

if __name__ == '__main__':

	#create instance of the tweepy tweet stream listener
	listener = TweetStreamListener()

	#set twitter keys/token from config.py file
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	#create instance of the tweepy stream
	stream = Stream(auth, listener)

	#search twtitter for "LEC" keyword
	stream.filter(track=['LEC'])