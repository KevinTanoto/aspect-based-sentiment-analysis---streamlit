from nltk import *
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
import json
from logging import raiseExceptions
import re
import string


# from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
# factory = StopWordRemoverFactory()
# stopwords = factory.get_stop_words()
# print(stopwords)

slangword_path = 'data/combined_slang_words.txt'

with open(slangword_path, 'r') as file:
    slang_word = file.read()
    slang_word = json.loads(slang_word)

dari = ["tdk", "gak", "ngga", "ga", "yg", "emng", "mmng", "k\
np", "stlh", "gara2", "krn", "hrs", "msh", "bkn", "yaa", "trs", "sdh", "\
untk",\
"dgn", "mksd", "gk", "y", "thn", "jd", "skrg", "samp\
e", "bapakk", 'dlm', 'cuuuy', "yg ", 'tak', 'kalo', 'sekrng', 'kek', 'gu\
e', 'sya', "kpd", 'alia', 'ama','banget']
hasil = ["tidak", "tidak", "tidak", "tidak", "yang", "memang\
", "memang", "kenapa", "setelah", "karena", "karena", "harus", "masih",\
"bukan", "ya", "terus", "sudah",\
"untuk", "dengan", "maksud", "tidak", "ya", "tahun"\
, "jadi", "sekarang", "sampai", "bapak", 'dalam', '', "yang ", 'tidak',\
'kalau', 'sekarang', 'seperti', 'kamu', 'saya', 'kepada', "alias", 'sama\
','sangat']
result_dict = dict(zip(dari, hasil))

slang_word.update(result_dict)

def cleaning_tweets(input):
    tweet = str(input)
    # remove link, mention, etc
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    tweet = re.sub(r'\$\w*', '', tweet)
    tweet = re.sub(r'$', '', tweet)
    tweet = re.sub(r'https?://[^\s\n\r]+', '', tweet)
    tweet = re.sub(r'https?://[A-Za-z0-9./]+','',tweet)
    tweet = re.sub(r'https//[A-Za-z0-9./]+','',tweet)
    tweet = tweet.replace("\n","")
    tweet = re.sub('@[\w]+', '', tweet)

    tweet = re.sub(r"n't", " not ", tweet)
    tweet = re.sub(r"\'s", " ", tweet)
    tweet = re.sub(r"\'ve", " have ", tweet)
    tweet = re.sub(r"\'re", " are ", tweet)
    tweet = re.sub(r"\'d", " would ", tweet)
    tweet = re.sub(r"\'ll", " will ", tweet)

    # remove emoji
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"
                           u"\U0001F300-\U0001F5FF"
                           u"\U0001F680-\U0001F6FF"
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           u"\U0001f926-\U0001f937"
                           u"\U00010000-\U0010ffff"
                           "]+", flags=re.UNICODE)
    tweet = emoji_pattern.sub(r'', tweet)

    # remove punctuation -> tidak digunakan untuk memperkuat akurasi Translate
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    tweet =  tweet.translate(translator)

    # remove excessive space
    tweet = re.sub(r'\s+', ' ', tweet)

    # case folding
    tweet = tweet.lower()
    tweet = tweet.strip()
    return tweet

def normalized_slang(text):
    tokens = word_tokenize(text)
    normalized_words = [slang_word.get(token, token) for token in tokens]
    # combined_string = ' '.join(normalized_words)
    return normalized_words

def remove_stopwords(text):
    stop_words = set(stopwords.words('indonesian'))
    # word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in text if not w in stop_words]
    return ' '.join(filtered_sentence)

def tokenize_tweet(text):
    tweet = cleaning_tweets(text)
    tweet = normalized_slang(tweet)
    tweet = remove_stopwords(tweet)
    if tweet == '':
      return None
    return word_tokenize(tweet)

def wc_format(df):
    df['new_text'] = df["full_text"].apply(tokenize_tweet)
    df_exploded = df.explode('new_text')

    combined_list = df_exploded['new_text'].tolist()
    combined_list = [word for word in combined_list if word is not None]

    return ' '.join(combined_list)
