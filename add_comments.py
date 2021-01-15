# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:29:36 2021

@author: Win10
"""

import pandas as pd
from datetime import datetime
import re
import nltk
from nltk.corpus import stopwords,words
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.stem import PorterStemmer
porter=PorterStemmer()
stop_words=stopwords.words("english")
lemmatizer=WordNetLemmatizer()

def clean(text):
  text=re.sub(r"[^a-zA-Z]"," ", text)
  
  tokens= word_tokenize(text)
  tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
  tokens=[porter.stem(word) for word in tokens]
  return tokens


def comment_adder():
    
    data = pd.read_csv('Comments.csv',index_col=0)
    username = input("Enter your UserName: ")
    comment = input("Enter your comment: ")
    t = datetime.now() 
    t = t.replace(microsecond=0)
    row = { "UserName" : username,
            "Comment":comment,
           "TimeStamp":t,
           "Replies" : [],
           "Keywords" : clean(comment)
           }
    data = data.append(row, ignore_index=True)
    
    data.to_csv("Comments.csv",index="False")
    
   
    
    