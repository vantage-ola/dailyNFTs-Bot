from flask import Flask
import tweepy
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

from api import fetch_data
import json

from time import sleep
from decouple import config


API_KEY = config('TWITTER_API_KEY')
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
    print("Authentication Failed")

data = fetch_data.NFT(freq="1d") #frequency -> daily


#data_collections = data.collections()



def deploy_tweet():
    data_nfts =  data.nfts()
    n = len(data_nfts)
    
    while n >= 0:
        try:
            n-=1
            

            
            for each in [data_nfts[n]]:
                tweet=f'''{each['nft_name']} sold for {each['price']} {each['date']} \nLink: {each['nft_url']}'''
                sleep(1)
                #print(tweet)
                api.update_status(tweet)
        except tweepy.TweepyException as  e:
            print(e)
            sleep(2)


app = Flask(__name__)

@app.route('/')
def job():
    deploy_tweet()
    print('Success')


scheduler = BackgroundScheduler()
scheduler.add_job(func=job, trigger="interval", seconds=60)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

if __name__ == "__main__":
    app.run(port=5000, debug=True)
