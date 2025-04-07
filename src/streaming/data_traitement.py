import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Télécharger les ressources NLTK
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Configurer les Stopwords et le Lemmatiser
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def nettoyer_texte(texte):
    # 1. Convertir en minuscules
    texte = texte.lower()

    # 2. Supprimer les URLs
    texte = re.sub(r'http\S+|www.\S+', '', texte)

    # 3. Supprimer les mentions (@user)
    texte = re.sub(r'@\w+', '', texte)

    # 4. Supprimer les hashtags (#hashtag)
    texte = re.sub(r'#\w+', '', texte)

    # 5. Supprimer les caractères spéciaux et chiffres
    texte = re.sub(r'[^a-zA-Z\s]', '', texte)

    # 6. Tokenisation
    tokens = re.split(r'\s+', texte)
    

    # 7. Suppression des stopwords et lemmatisation
    tokens_propres = [lemmatizer.lemmatize(mot) for mot in tokens if mot not in stop_words]

    # 8. Reconstruction du texte nettoyé
    texte_nettoye = " ".join(tokens_propres)

    return texte_nettoye
