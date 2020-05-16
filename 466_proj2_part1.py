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
from pprint import pprint

records = list(df.text)
number_selected = len(records) // 16  #TODO CHANGE THIS VALUE TO 4
selected_records = random.sample(records, number_selected) #get random sample of number_selected records without replacement

utterances = [record for record in selected_records] #get all the utterance fields only (column #15) for clustering
print("total number of points:",len(utterances))

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords 
from nltk.corpus import wordnet 
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

wordnet_lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english')) 
punctuation = "-!?;:\"\'.,"

def getPOS(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

def getFeatures(text):
    features = {}
    tokens = nltk.word_tokenize(text.lower())
    tot_cnt = len(tokens)
    for word in tokens:        
        if word not in stop_words and word not in punctuation:
            w = wordnet_lemmatizer.lemmatize(word, getPOS(word))
            if w not in features:
                features[w] = 1/float(tot_cnt)
            else:
                features[w] += 1/float(tot_cnt)
    return features

data = df['text']
data = data[:2]

getFeatures(data[0])
data

import numpy as np
import random, sys
from collections import Counter

max_t = 2   # max itterations (ignores threshold) (-1 to unset)
k = 2
M = []
M.append([0 for i in range(0, k)])

def initCentroids(vec_data, k):
    centroidID = np.random.permutation(len(vec_data))[:k]
    return [id for id in centroidID]

def calculateDistance(v_dict, u_dict):
    v = list(v_dict.values())
    u = list(u_dict.values())
    total = 0
    for i in range(0, len(v)):
        total += ((v[i] - u[i]) ** 2)
    return np.sqrt(total)


# takes a vector dictionary and a set of all the keys
# returns a new vector dictionary with all the keys
def reshapeVectDict(vect_dict, keys):
    old_shape = len(vect_dict)
    for key in keys:
        if key not in vect_dict:
            vect_dict[key] = 0.0
    return vect_dict

# For a given point, find the closest centroid from the list, return centroid's index
def closestCentroid(point, centroids):
    # Get all the keys (words) in the point and centroids
    # This will be used to transform them to the same dimension so we can do math
    all_keys = []
    all_keys.extend(point)        
    for centroid in centroids:        
        all_keys.extend(centroid.keys())
    all_keys = set(all_keys)

    closestCentroid = 0
    minDist = sys.maxsize
    point_reshape = reshapeVectDict(point, all_keys)

    for centroid in centroids:
        centroid_reshape = reshapeVectDict(centroid, all_keys)
        dist = calculateDistance(point_reshape, centroid_reshape)

        if (dist < minDist):
            minDist = dist
            closestCentroid = centroids.index(centroid)

    return closestCentroid


def k_means(vec_data, k, e):
    t = 0
    M[t] = initCentroids(vec_data, k)

    if max_t >= 0:        
        while (t < max_t):
            t += 1
            C = []
            for i in range(0, k):
                C.append([])
            # Centroid assignment
            for point in vec_data:
                clusterID = closestCentroid(point, M[t])

data = selected_records
vec_data = [getFeatures(text) for text in data]

k_means(vec_data, 2, 1)

# M holds the centroid IDs
M

# vec_data contains all the vectorized data
# initialize centroids
centroids = [vec_data[c] for c in initCentroids(vec_data, 2)]
pprint(centroids)

point = vec_data[0]

centroidID = closestCentroid(point, centroids)
print("point is closest to the centroid, ", centroidID)
print("point: ")
print(point)
print("closest centroid: ")
print(centroids[centroidID])
print("other centroids: ")
print([c for c in centroids if not centroids.index(c) == centroidID])

total = 0
total += (1 - 2) ** 2
total



# Python program to combine two dictionary 
# adding values for common keys 
from collections import Counter   
  
# adding the values with common key 
          
Cdict = Counter(dict_1) + Counter(dict_2) 
print(Cdict)

keys = ['a','b','c']
dict_2 = {i:0 for i in keys}
print(dict_2)
dict_1 = {}
dict_1['a'] = 23

Cdict = Counter(dict_1) + Counter(dict_2) 
Cdict

all_keys = []
for centroid in centroids:
    all_keys.extend(centroid.keys())
all_keys = set(all_keys)

vec1 = []
vec2 = []
for key in all_keys:
    if key not in dict_1:
        vec1.append(0)
    else:
        vec1.append(dict_1[key])
    if key not in dict_2:
        vec2.append(0)
    else:
        vec2.append(dict_2[key])

print(vec1)
print(vec2)
a = np.matrix(vec1)
b = np.matrix(vec2)
ret = a - b
print(ret)

# Python Program illustrating  
# numpy.mean() method    
import numpy as np 
    
  
# 2D array  
arr = [[2,10],   
       [2,10]]
       
    
# mean of the flattened array  
print("\nmean of arr, axis = None : ", np.mean(arr))