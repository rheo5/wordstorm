import urllib.request
from bs4 import BeautifulSoup
import spacy
from nltk.corpus import stopwords
from gensim.models import Word2Vec

def isValid(word):
    return word.isalpha()

def train_source(keyword, source):
    html_content = urllib.request.urlopen(source).read()
    soup = BeautifulSoup(html_content, 'html.parser')
    text_content = soup.get_text()

    nlp = spacy.load('en_core_web_sm')
    processed_text = nlp(text_content)

    processed_sentences = [sent.lemma_.split() for sent in processed_text.sents]

    interchangeable_words_model = Word2Vec(
        sentences=processed_sentences,
        min_count=10, # Purning the internal dictionary
        vector_size=400, # the number of dimensions (N) gensim maps the word onto
        window=4, # Define when two words are together, 2 means, 2 words left and 2 words right
        compute_loss=True,
        sg=1
    )

    stop_words = set(stopwords.words('english'))
    stop_words_lower = set(map(str.lower, stop_words))  # Convert stop words to lowercase

    filtered_similar_words = []

    if keyword in interchangeable_words_model.wv.key_to_index:
        similar_words_lower = [(w, sim) for w, sim in interchangeable_words_model.wv.most_similar(keyword, topn=30)]
    else:
        similar_words_lower = [("TryAgain", 0.1)]

    seen = set()
    for w, sim in similar_words_lower:
        if isValid(w) and w not in stop_words_lower and w not in stop_words and w.lower() not in seen:
            filtered_similar_words.append(w)
            seen.add(w.lower())

    return filtered_similar_words