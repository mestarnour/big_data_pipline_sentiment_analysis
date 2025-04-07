from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from analyse_sentiment import sentiment_udf
from pyspark.sql.types import StringType
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pyspark.sql.types import StructType, StructField
from pyspark.sql.functions import from_json
from elasticsearch import Elasticsearch

# Création de la session Spark
spark = SparkSession.builder \
    .appName("TwitterSentimentAnalysis") \
    .config("spark.master", "spark://spark:7077") \
    .config("spark.sql.streaming.checkpointLocation", "/tmp/spark-checkpoint") \
    .getOrCreate()

# Connexion à Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Définition du schéma des tweets
tweet_schema = StructType([
    StructField("id", StringType(), True),
    StructField("text", StringType(), True)
])

# Analyse des sentiments avec VADER
analyser = SentimentIntensityAnalyzer()
def detecter_sentiment(texte):
    score = analyser.polarity_scores(texte)
    if score['compound'] >= 0.05:
        return "Positif"
    elif score['compound'] <= -0.05:
        return "Négatif"
    else:
        return "Neutre"

# Définir la fonction UDF pour Spark
sentiment_udf = udf(detecter_sentiment, StringType())

# Lecture du flux Kafka
KAFKA_BROKER = "kafka:9092"
KAFKA_TOPIC = "tweets"

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", KAFKA_BROKER) \
    .option("subscribe", KAFKA_TOPIC) \
    .option("startingOffsets", "earliest") \
    .load()

# Conversion du JSON en colonnes exploitables
df = df.selectExpr("CAST(value AS STRING)")
df = df.withColumn("json_data", from_json(col("value"), tweet_schema)).select("json_data.*")

# Ajout de la colonne sentiment avec Spark UDF
df = df.withColumn("sentiment", sentiment_udf(col("text")))

# Fonction d'écriture dans Elasticsearch
def envoyer_a_elasticsearch(batch_df, batch_id):
    for row in batch_df.collect():
        doc = {
            "id": row["id"],
            "text": row["text"],
            "sentiment": row["sentiment"]
        }
        es.index(index="tweets_sentiments", body=doc)

# Écriture en continu
query = df.writeStream \
    .foreachBatch(envoyer_a_elasticsearch) \
    .start()

query.awaitTermination()