import json
import nltk
import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string

lemmer = nltk.stem.WordNetLemmatizer()
remove_punctuation = dict((ord(punct), None) for punct in string.punctuation)

def get_corpus():
    with open('data/obama.json') as f:
        data = json.load(f)

    return data

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punctuation)))


def response(user_response):
    robo_response=''
    sentence_tokens.append(user_response)

    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sentence_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sentence_tokens[idx]
        return robo_response


if __name__ == '__main__':
    data = get_corpus()
    sentence_tokens = data['sentence_tokens']
    flag = True

    while(flag==True):
        user_response = str(input())
        user_response=user_response.lower()

        if(user_response!='bye'):
            if(user_response=='thanks' or user_response=='thank you' ):
                flag=False
                print("Chatbot: You are welcome.")
            else:
                print("Chatbot: ")
                print(response(user_response))
                sentence_tokens.remove(user_response)
        else:
            flag=False
            print("Chatbot: Bye! take care.")
