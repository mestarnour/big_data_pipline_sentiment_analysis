from elasticsearch import Elasticsearch

# Connexion à Elasticsearch
es = Elasticsearch(
    "http://localhost:9200",
    basic_auth=("elastic", "changeme") ,
    verify_certs=False 
)

# Création de l'index
index_name = "tweets_sentiments"
mapping = {
    "mappings": {
        "properties": {
            "id": {"type": "keyword"},
            "text": {"type": "text"},
            "sentiment": {"type": "keyword"},
            "timestamp": {"type": "date"}
        }
    }
}

# Vérifier si l'index existe avant de le créer
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, body=mapping)
    print(f"Index {index_name} créé avec succès !")
else:
    print(f"L'index {index_name} existe déjà.")
