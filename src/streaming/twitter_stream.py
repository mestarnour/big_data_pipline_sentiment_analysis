import pandas as pd
from kafka import KafkaProducer
import json
import time

# Configuration
CSV_FILE = 'data/twitter_training.csv'  
KAFKA_BROKER = '192.168.13.99:9092' #utilse l'adresse ip dans mon hote 
KAFKA_TOPIC = 'tweets'

# Connexion à Kafka
producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

# Lecture du fichier CSV
df = pd.read_csv(CSV_FILE)

# Envoi des tweets ligne par ligne
for index, row in df.iterrows():
    tweet = {
         'id': str(row[0]),  # Conversion en string pour éviter les erreurs de sérialisation
         'name': str(row[1]),
         'label': str(row[2]),
         'text': str(row[3])
    }
    producer.send(KAFKA_TOPIC, value=tweet)
    print(f"Tweet envoyé : {tweet}")
    time.sleep(1)  # Pause de 1 seconde entre chaque envoi

# Fermeture du producer
producer.flush()
producer.close()
