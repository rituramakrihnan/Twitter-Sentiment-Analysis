import csv
import json

import tweepy

# credentials
consumer_key = "IXtII6Xvlw86cTjgpySiKejtM"
consumer_secret = "vOngQO198QKG4kbNDOFGht0hZK2XX4SIY7C9ogadBfL9IR0zSb"
access_token = "1618106344091049985-HOZqekeoLhE7unIsmrghKOqy6VU1fn"
access_token_secret = "K2dwCFPXyic2wkCO9bd1L8KEl4lUWch5BVWDQA03jzNCc"

# authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Creation of the actual interface, using authentication
api = tweepy.API(auth, wait_on_rate_limit=True)

tweets = []
for tweet in tweepy.Cursor(api.search_tweets,
                           q="",
                           include_ext_edit_control='true',
                           locale='en',
                           result_type='recent',
                           until='2023-02-21',
                           include_entities='true',
                           geocode="37.0902,-95.7129,25000km",
                           lang="en").items(5):

    tweets.append(tweet._json)

with open('tweets_data.json', 'w') as out:
    json.dump(tweets, out)
