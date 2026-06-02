# Big Data Pipeline for Social Media Sentiment Analysis

## Authors & Supervision

- **Authors:** Nourelhouda Mestar and Messaoudi Rym Sara
- **Institution:** ENSTTIC – Mass Data Processing and Analysis

---

## Description

This project implements a Big Data pipeline designed for the real-time collection, processing, analysis, and visualization of sentiments expressed in tweets (positive, negative, or neutral).

The architecture is built on Apache Kafka, Apache Spark, Elasticsearch, and Kibana, featuring NLP analysis via VADER. Due to Twitter API access constraints, tweets are simulated using a Kaggle dataset. This project demonstrates the integration of Big Data technologies for handling massive data streams and visualizing results in real time.

---

## Features

- Continuous tweet ingestion via Kafka.
- Automated text cleaning including removal of links, mentions, special characters, and hashtags.
- NLP sentiment analysis using VADER.
- Data storage and indexing in Elasticsearch.
- Interactive visualization with Kibana dashboards.
- Modular and scalable architecture.

---

## Technologies Used

- **Apache Kafka:** Ingestion and streaming of tweets.
- **Apache Spark:** Distributed real-time processing (optional in lightweight version).
- **VADER / NLTK:** Sentiment analysis.
- **Elasticsearch:** Textual indexing and search engine.
- **Kibana:** Result visualization platform.
- **Docker:** Service orchestration and containerization.

---

## Project Structure

```text
config/           # Configuration files (docker-compose.yml, etc.)
data/             # Datasets (CSV, Kaggle)
src/
 └── streaming/   # Python scripts: producer, consumer, cleaning, and analysis

