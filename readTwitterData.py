from tweepy import OAuthHandler
import tweepy
from tweepy.streaming import StreamListener
import json
import time
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
#load vader data set
try:
	nltk.download('vader_lexicon')
	nltk.download('punkt')
except:
	pass
#consumer key, consumer secret access token access secret
consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

#create a twitter streaming function to download all the message from the 
#twitter profile

class MyStreamListner(StreamListener):
	
	def on_data(self, data):
		sid = SentimentIntensityAnalyzer()
		all_data = json.loads(data)
		tweet = all_data["text"]
		#ss = sid.polarity_scores(tweet)
		analysis = TextBlob(tweet)
		print(analysis)
		print(analysis.sentiment,analysis.sentiment.polarity)
		print(analysis.detect_language())
		time.sleep(2)
		return True
	
	def on_status(self, status):
		print(status)
	
	def on_error(self, status):
		print(status)

#now use oAuth to login in the twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



#api.update_status('tweepy + oauth!')

#myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = auth, listener=MyStreamListner())
myStream.filter(track=['Arsenal'])

name = "thermax"
#public_tweets = api.search(q="thermax")

#public_tweets = api.home_timeline()
'''
for tweet in public_tweets:
	print(tweet.text)	
	time.sleep(2)
'''
