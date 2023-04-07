import os
import csv
import tweepy as tw
from dotenv import load_dotenv

apikey = "32GUG2ek0MBmJdCDrNTj5LHpU"
apisecretkey = "JhfMnuQH1yyQJSyi07ByhbB4YmnLOTEpQrgB7DQittWBqmtFkH"
accesstoken = "1370826631825166336-CuHWx6CU9lDqvUkApD7R2KEzUNVWry"
accesstokensecret = "SRlTs8J8DgHO3kwnz5oDQiEoBMUmgySRp8QVZUaVUTn06"

auth = tw.OAuthHandler(apikey, apisecretkey)
auth.set_access_token(accesstoken, accesstokensecret)
api = tw.API(auth, wait_on_rate_limit=True)

search_word = 'chatgpt'
tweets = tw.Cursor(api.search_tweets, q=search_word, lang='en', tweet_mode='extended').items(1000)
tweet_details = [[tweet.text, tweet.user.screen_name, tweet.user.location] for tweet in
                 tweets]
tweet_header = ['Text', 'Name', 'Location']

with open('tweets.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(tweet_header)
    writer.writerows(tweet_details)
