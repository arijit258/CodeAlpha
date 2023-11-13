import pickle
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer 

ss = SnowballStemmer("english")
nltk.download('stopwords')

model=pickle.load(open('best_model.pkl','rb'))
vectorizer=pickle.load(open('vectorizer.pkl','rb'))

def remove_stopwords(text):
    sw = stopwords.words('english')
    txt = [word.lower() for word in text.split() if word.lower() not in sw]
    return txt 


def stemming(text) : 
    text = [ss.stem(word) for word in text if word.split()]
    return "".join(text)

def transform_data(text):
    text=remove_stopwords(text)
    text=stemming(text)
    return pd.DataFrame(vectorizer.transform([text]).todense())

msg=input('Enter sms to send : ')
print(model.predict(transform_data(msg)))
