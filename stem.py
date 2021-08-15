# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:31:50 2019

@author: n.sharma
"""


import re
import string

from nltk import sent_tokenize
from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

filename = 'metamorphosis_clean.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

# split into words by white space
words = text.split()
words = [word.lower() for word in words]
# prepare regex for char filtering
re_punc = re.compile('[%s]' % re.escape(string.punctuation))
# remove punctuation from each word
stripped = [re_punc.sub('', w) for w in words]
#print(stripped)


#sentences = sent_tokenize(text)
#print(sentences[0])

# split into words
tokens = word_tokenize(text)
tokens = [w.lower() for w in tokens]
stripped = [re_punc.sub('', w) for w in tokens]
words = [word for word in stripped if word.isalpha()]


print("All stop words")
stop_words = stopwords.words('english')
print(stop_words)
words = [w for w in words if not w in stop_words]
#print(words)


# stemming of words
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in words]
#print(stemmed)