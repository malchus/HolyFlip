import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

kjv = open("kjv.txt","r")
token = nltk.word_tokenize(kjv.read())
bigrams = ngrams(token,2)
trigrams = ngrams(token,3)



print (Counter(trigrams))