from requests_oauthlib import  OAuth1Session
import json
import time
import pandas as pd


CK = 'A7ZKx6ox4DExBK5K2IyCdIFML'
CS = 'vTkie5DCJLRduiXINAPuPJjJvvJzbkw8ZapEHU6TWU0EhlmmzD'
AT = '1391261478-q2ijsReuvVKAdEjbTdn1RWL54D6bTg1QoaCrorB'
AS = 'bEdvsea3gggJxv3mg5KTWArgDCskNQkD3Ahx5Pf9nNYih'

url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

params = {'count': 100}

TweetList = []

twitter = OAuth1Session(CK, CS, AT, AS)

for i in range(100):
    print("i:%d " % i)
    req = twitter.get(url, params = params)
    if req.status_code == 200:
        timeline = json.loads(req.text)
        for tweet in timeline:
            TweetList.append(tweet["text"])
    else:
        print ("Error: %d" % req.status_code)
    time.sleep(240)

df = pd.DataFrame(TweetList)
df.to_csv('twitter.csv')


