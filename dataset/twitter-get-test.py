# coding:utf-8

from requests_oauthlib import  OAuth1Session
import json, datetime, time
import sys, ConfigParser
import pandas as pd

#'''
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
 
url = 'https://api.twitter.com/1.1/search/tweets.json'
res = session.get(url, params = {'q':u'iPhoneX', 'count':10})
 
if res.status_code != 200:
    print ("Twitter API Error: %d" % res.status_code)
    sys.exit(1)

print ('アクセス可能回数 %s' % res.headers['X-Rate-Limit-Remaining'])
print ('リセット時間 %s' % res.headers['X-Rate-Limit-Reset'])
sec = int(res.headers['X-Rate-Limit-Reset'])\
           - time.mktime(datetime.datetime.now().timetuple())
print ('リセット時間 （残り秒数に換算） %s' % sec)

res_text = json.loads(res.text)
for tweet in res_text['statuses']:
    print ('-----')
    print (tweet['created_at'])
    print (tweet['text'])

