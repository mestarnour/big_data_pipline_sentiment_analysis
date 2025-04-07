from kafka import KafkaConsumer
import json
from data_traitement import nettoyer_texte
from analyse_sentiment import analyser_sentiment
from elasticsearch import Elasticsearch
import datetime

# Configuration
KAFKA_BROKER ='192.168.13.99:9092'  
KAFKA_TOPIC = 'tweets'

es = Elasticsearch(
    "http://localhost:9200",
    basic_auth=("elastic", "changeme") ,
    verify_certs=False 
)  
index_name = "tweets_sentiments"

# Connexion au consumer Kafka
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=[KAFKA_BROKER],
    auto_offset_reset='earliest',  # Pour lire depuis le début du topic
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("En attente de tweets...")

# Lecture des messages en continu
for message in consumer:
    tweet = message.value
    texte_original = tweet.get('text') 
    texte_nettoye = nettoyer_texte(texte_original)
    sentiment = analyser_sentiment(texte_nettoye)  
        # Document à stocker
    doc = {
        "id": tweet.get('id'),
        "text": texte_nettoye,
        "sentiment": sentiment,
        "timestamp": datetime.datetime.now()
    }

    es.index(index=index_name, body=doc)

    print(f"\nTweet original : {texte_original}")
    print(f"Tweet nettoyé  : {texte_nettoye}")
    print(f"Sentiment      : {sentiment}")
    print(f"Stocké dans Elasticsearch ✅")
    
