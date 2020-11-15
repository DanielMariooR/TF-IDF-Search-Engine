import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from bs4 import BeautifulSoup

import os
import math

def cosine_similiarity(vector1,vector2,vector3):
#{Menghitung cosine similarity dari 2 buah vector}
    n = len(vector1)
    result = 0
    for i in range(n):
        result += (vector1[i]*vector2[i])
    if(magnitude(vector1)==0 or magnitude(vector3)==0):
        return 0
    else:
        return (result/(magnitude(vector1)*magnitude(vector3)))

def magnitude(vector):
#{Menghitung besar sebuah vektor}
    magnitude = 0
    for elem in vector:
        magnitude += (elem ** 2)
    return math.sqrt(magnitude)

query = "what is cloud computing?"

def Preprocessing(text):
#{Fungsi yang menerima text dan melakukan stemming serta stop word removal}
#{Mengembalikan list berisi kata-kata yang telah diproses}
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    
    token = word_tokenize(text)
    filtered = []
    for word in token:
        if word not in stop_words:
            filtered.append(ps.stem(word))
    return filtered


def Del_Dupl(bag_of_words):
#{Menghapus kata kata duplikat pada bag of words}
    bag_of_words = list(dict.fromkeys(bag_of_words))
    return bag_of_words

def Querylib(query):
#{Menghasilkan library kata-kata dari query}
#{Digunakan untuk mengubah text/dokumen menjadi bentuk vektor}
    querylib = Del_Dupl(query)
    return querylib

def Vectorizer(querylib,bag_of_words):
#{Mengubah array berisi kata-kata menjadi vektor yang dapat dihitung dalam cosine similarity}
#{Parameter fungsi berupa library kata-kata dan array yang berisi kata kata yang telah di preprocessing}
    n = len(querylib)
    vector = [0 for i in range(n)]
    
    for i in range(n):
        for word in bag_of_words:
            if querylib[i] == word:
                vector[i] += 1
    return vector

def HtmlParser(soup):
    text = soup.find_all('p')
    for i in range(len(text)):
        text[i] = text[i].get_text()
    return " ".join(text)

def HtmlTitleParse(soup):
    title = soup.find_all('title')[0].get_text()
    return title

def Sort(results):
#{Mengurutkan hasil pencarian dari yang memiliki nilai cosine similiarity terbesar ke yang terkecil}
    for i in range(len(results)-1):
        key = i
        for j in range(len(results)-1,i,-1):
            if results[key][0] < results[j][0]:
                key = j
        results[i],results[key] = results[key],results[i]

def Wcounter(text):
#{Menghitung jumlah kata pada setiap dokumen/artikel}
    token = word_tokenize(text)
    return len(token)

def getFirstSen(text):
    firstSen = text.partition('.')[0] + '.'
    return firstSen