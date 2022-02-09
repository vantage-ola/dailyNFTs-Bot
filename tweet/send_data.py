import tweepy
from decouple import config

import json
from datetime import datetime
from time import sleep

#today's date
today_date = datetime.now().date()

#open data
f= open(f'api/data/{today_date}-nfts-daily.json') #* path 

#twitter credentials
API_KEY = config('API_KEY')
API_KEY_SECRET = config('API_KEY_SECRET')
ACCESS_TOKEN = config('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = config('ACCESS_TOKEN_SECRET')



auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")


def tweet_data():
    data = json.load(f)
    n = len(data)
    print(n)
    while n >= 0:
        n-=1
        try:
            for each in [data[n]]:
                tweet=f'''{each['nft_name']} sold for {each['price']} {each['date']} \nLink: {each['nft_url']}'''
                print(tweet)
                #api.update_status(tweet)
                 #delay next post for 1 minute
        except tweepy.TweepyException as  e:
            print(e.reason)
            sleep(2)

if __name__ == '__main__':
    tweet_data()