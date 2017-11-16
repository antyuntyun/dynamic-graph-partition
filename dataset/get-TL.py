# coding:utf-8

from requests_oauthlib import  OAuth1Session
import json, datetime, time
import sys, ConfigParser
import pandas as pd

#read config file
config = ConfigParser.SafeConfigParser()
try:
    config.read('twitter.conf')
    CK = config.get('twitter', 'CK')
    CS = config.get('twitter', 'CS')
    AT = config.get('twitter', 'AT')
    AS = config.get('twitter', 'AS')   
except:
    print "Error occured in reading config"
    exit()
print ("CK: " + CK)
print ("CS: " + CS)
print ("AT: " + AT)
print ("AS: " + AS)
session = OAuth1Session(CK, CS, AT, AS)
 
url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
params = {'count': 100}

TweetList = []

for i in range(1):
    req = session.get(url, params = params)
    if req.status_code == 200:
        timeline = json.loads(req.text)
        for tweet in timeline:
            TweetList.append(tweet["text"])
    else:
        print ("Error: %d" % req.status_code)
#    time.sleep(240)

df = pd.DataFrame(TweetList)
df.to_csv('TweetList.csv',encoding="utf-8")
