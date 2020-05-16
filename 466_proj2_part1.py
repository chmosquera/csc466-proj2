# -*- coding: utf-8 -*-
"""466-proj2-part1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qw9ktmDdSpLdZfTVtl6yg3w54lpRIMWr
"""

path = "drive/My Drive/Colab Notebooks/466-proj2/"
f = open(path + 'readme.txt', 'r')
print(f.read())
f.close()

FILE = "committee_utterances.tsv"

import pandas as pd

df = pd.read_csv(path + FILE, sep='\t')
df

#Select a random 25% (1/4) of the content
import random

records = list(df.text)
number_selected = len(records) // 16  #TODO CHANGE THIS VALUE TO 4
selected_records = random.sample(records, number_selected) #get random sample of number_selected records without replacement

utterances = [record for record in selected_records] #get all the utterance fields only (column #15) for clustering
print("total number of points:",len(utterances))

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords 
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

wordnet_lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english')) 
punctuation = "-!?;:\"\'.,"

def getFeatures(text):
    features = {}
    tokens = nltk.word_tokenize(text)
    for word in tokens:        
        if word not in stop_words and word not in punctuation:
            w = wordnet_lemmatizer.lemmatize(word)
            if w not in features:
                features[w] = 1
            else:
                features[w] += 1            
    return features

def computeTF(word_dict, all_words):
    tf = {}
    total_words = len(set(all_words))
    for word, count in word_dict.items():
        tf[word] = count / float(total_words)
    return tf  

import math
def computeIDF(docs):
    idf = {}
    n = len(docs)
    for d in docs:
        for word,value in d.items():
            if value > 0:
                if word not in idf:                  
                    idf[word] = 1
                else:
                    idf[word] += 1
    for word,value in idf.items():
        idf[word] = math.log(n/float(value))
    return idf

def computeTFIDF(tf_all_words, idfs):
    tfidf = {}
    for word, val in tf_all_words.items():
        tfidf[word] = val * idfs[word]
    return tfidf

def tfidf_vectorizer(feature_analyzer, data):
    # Get features
    data_dict = []
    for sample in data:
        feats = feature_analyzer(sample)
        data_dict.append(feats)
    # Get TFIDF
    matrix = []
    idf = computeIDF(data_dict)
    tfidf = computeTFIDF(computeTF())
    matrix.append()

feats1 = getFeatures(df.text[0])
feats2 = getFeatures(df.text[2])
feats3 = getFeatures(df.text[3])
FEATS = []
FEATS.append(feats1)
FEATS.append(feats2)
FEATS.append(feats3)
SET = set(feats1).union(set(feats2)).union(set(feats3))

computeTFIDF(computeTF(set2, SET), computeIDF(FEATS))

def initialize_centroids(D, k)

def k-means(D, k, e):

data = df['text']
data = data[:2]

tfidf_vectorizer(getFeatures, data)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize
data = df['text']
data = data[:2]

tf_idf_vectorizor = TfidfVectorizer(stop_words = 'english',#tokenizer = tokenize_and_stem,
                             max_features = 20000)
tf_idf = tf_idf_vectorizor.fit_transform(data)
tf_idf_norm = normalize(tf_idf)
tf_idf_array = tf_idf_norm.toarray()
print(len(data[0].split()), data[0])
print(len(data[1].split()), data[1])
print(tf_idf_array)