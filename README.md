# 📊 Pipeline Big Data pour l'Analyse de Sentiments sur les Réseaux Sociaux

## 📌 Description
Ce projet met en place un pipeline Big Data permettant la **collecte**, le **traitement**, l’**analyse** et la **visualisation** en temps réel des sentiments exprimés dans des tweets (positif, négatif, neutre).  
L’architecture repose sur **Apache Kafka**, **Apache Spark**, **Elasticsearch** et **Kibana**, avec une analyse NLP via **VADER**.

En raison de contraintes d’accès à l’API Twitter, les tweets sont simulés à partir d’un dataset Kaggle.  
Ce projet illustre l’intégration de technologies Big Data pour le traitement de flux massifs et la visualisation des résultats en temps réel.

---

## 🚀 Fonctionnalités
- Ingestion en continu des tweets via **Kafka**
- Nettoyage automatique du texte (liens, mentions, caractères spéciaux, hashtags)
- Analyse NLP des sentiments avec **VADER**
- Stockage des résultats dans **Elasticsearch**
- Visualisation interactive avec **Kibana**
- Architecture modulaire et scalable

---

## 🛠️ Technologies utilisées
- **Apache Kafka** : ingestion et streaming des tweets  
- **Apache Spark** : traitement distribué et en temps réel (optionnel dans la version légère)  
- **VADER / NLTK** : analyse de sentiments  
- **Elasticsearch** : indexation et recherche textuelle  
- **Kibana** : visualisation des résultats  
- **Docker** : orchestration des services

---

## 📂 Structure du projet
```
config/           # Fichiers de configuration (docker-compose.yml, etc.)
data/             # Jeux de données (CSV, Kaggle)
src/
 └── streaming/   # Scripts Python : producteur, consommateur, nettoyage, analyse
```

---

## ⚙️ Installation & Exécution

### 1️⃣ Cloner le dépôt
```bash
git clone <url_du_projet>
cd projet-sentiment-analysis
```

### 2️⃣ Lancer les services Docker
```bash
docker-compose -f config/docker-compose.yml up -d
```
Services démarrés :
- Kafka (port 9092)
- Elasticsearch (port 9200)
- Kibana (port 5601)
- Spark (si utilisé)

### 3️⃣ Installer les dépendances Python
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

### 4️⃣ Démarrer le pipeline
- **Producteur Kafka** (simulation de tweets) :
```bash
python src/streaming/twitter_stream.py
```
- **Consommateur Kafka** (nettoyage + analyse + stockage) :
```bash
python src/streaming/consumer_kafka.py
```

---

## 📊 Visualisation
Accéder à Kibana : [http://localhost:5601](http://localhost:5601)  

Tableaux de bord disponibles :
- Répartition des sentiments (positif / négatif / neutre)
- Évolution temporelle des sentiments
- Nuage de mots et tendances

---

## 🔍 Fonctionnement global
1. **Collecte des tweets** : récupération via dataset Kaggle ou API (si disponible)  
2. **Kafka Producer** : envoi des tweets vers un topic Kafka  
3. **Kafka Consumer + Nettoyage** : suppression des éléments non pertinents et normalisation du texte  
4. **Analyse de sentiments** : attribution d’une polarité à chaque tweet (Positif, Négatif, Neutre)  
5. **Stockage dans Elasticsearch** : indexation pour recherche rapide  
6. **Visualisation avec Kibana** : graphiques et dashboards interactifs  

---

## 📝 Conclusion
Dans ce projet, nous avons mis en place un pipeline Big Data pour l’analyse des sentiments des tweets en temps réel.  
Malgré certaines contraintes techniques (accès API Twitter payant, configuration Spark complexe sous Docker), nous avons trouvé des solutions alternatives efficaces, notamment :
- Simulation des tweets via un dataset Kaggle
- Analyse des sentiments avec **VADER**, légère mais performante pour ce type de flux

Grâce à cette architecture, nous avons pu collecter, analyser et visualiser en temps réel les opinions exprimées sur les réseaux sociaux.  
Ce projet illustre l’importance d’adapter les outils aux contraintes tout en maintenant les objectifs techniques et fonctionnels.

---

## 👥 Auteurs
- **Mestar NourEl Houda**
- **Messaoudi Rym Sara**  
ENSTTIC – Traitement et Analyse de Données Massives
