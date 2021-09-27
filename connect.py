from TwitterSearch import *
from pymongo import MongoClient

ts= TwitterSearch(
    consumer_key = consumer_key,
    consumer_secret = consumer_secret,
    access_token = access_token,
    access_token_secret = access_token_secret
)

client = MongoClient(Name_local) 

tso = TwitterSearchOrder()
tso.set_keywords(['marvel','heroi da marvel'], or_operator=True)
tso.set_language('pt')

db = client.Data_Challenge_Dev

for tweet in ts.search_tweets_iterable(tso): 

    print('created_at:', tweet['created_at'],'User:',tweet['id_str'] ,'Tweet: ',tweet['text'])

    texto = tweet['text']

    db.texto.insert_many(
        [
            tweet
        ]
    )

