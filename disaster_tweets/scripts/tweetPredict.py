import nltk
import spacy
import re
import pickle
import os
import math
from pathlib import Path

### Return lemmatized text

def lemmatize_text(text):
    w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
    lemmatizer = nltk.stem.WordNetLemmatizer()
    return ' '.join([lemmatizer.lemmatize(w) for w in w_tokenizer.tokenize(text)])

### Returns an array from preprocessed tweet text for fitting in model

def preprocess(text):
    here = Path(__file__).parent
    # lowercase
    text = text.lower()
    # removing links, mentions, and hashtag (only the symbol)
    text = re.sub(r'https?://\S+|www\.\S+','', text)
    text = re.sub(r'@[A-Za-z0-9]+','', text)
    text = re.sub(r'#','', text)
    # removing punctuation
    text = re.sub(r'[^\w\s]','', text)
    # lemmatizing text
    text = lemmatize_text(text)
    # removing stopwords
    all_stopwords = set(nltk.corpus.stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in (all_stopwords)])
    # removing words with numbers and letters along
    text = ' '.join(w for w in text.split() if not any(j.isdigit() for j in w))
    vect = pickle.load(open(here/'../models/vectorizer.sav', 'rb'))
    text = vect.transform([text])
    return text.todense()

### Returns a probability of tweet being about real disaster

def predict(text):
    here = Path(__file__).parent
    clf_LogReg = pickle.load(open(here/'../models/LogReg_model.sav', 'rb'))
    clf_RF = pickle.load(open(here/'../models/RF_model.sav', 'rb'))
    clf_NB = pickle.load(open(here/'../models/NB_model.sav', 'rb'))
    text = preprocess(text)
    predict_LogReg = clf_LogReg.predict_proba(text)[:, 1]
    predict_RF= clf_RF.predict_proba(text)[:, 1]
    predict_NB = clf_NB.predict_proba(text)[:, 1]
    return math.floor(((predict_LogReg + predict_RF + predict_NB) / 3)[0] * 100) / 100