from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Télécharger les ressources nécessaires pour VADER
nltk.download('vader_lexicon')

# Initialiser l'analyseur de sentiments
sia = SentimentIntensityAnalyzer()

def analyser_sentiment(texte):
    """Analyse le sentiment d'un tweet et retourne Positif, Négatif ou Neutre."""
    score = sia.polarity_scores(texte)['compound']  # Score global du sentiment
    
    if score >= 0.05:
        return "Positif"
    elif score <= -0.05:
        return "Négatif"
    else:
        return "Neutre"

