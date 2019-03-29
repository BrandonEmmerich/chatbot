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
    with open('data/presidents.json') as f:
        data = json.load(f)

    return data

def LemNormalize(text):
    cleaned_text = text.lower().translate(remove_punctuation)
    tokens = nltk.word_tokenize(cleaned_text)
    lemmatized_tokens = [lemmer.lemmatize(token) for token in tokens]

    return lemmatized_tokens

def chatbot_response(user_input):
    robo_response=''
    sentence_tokens.append(user_input)

    tfidf_matrix = vectorizer.fit_transform(sentence_tokens)
    cosine_similarity_values = cosine_similarity(tfidf_matrix[-1], tfidf_matrix)
    index=cosine_similarity_values.argsort()[0][-2]

    flat = cosine_similarity_values.flatten()
    flat.sort()
    token_tfidf = flat[-2]

    if(token_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        sentence_tokens.remove(user_input)

        return robo_response

    else:
        robo_response = robo_response+sentence_tokens[index]
        sentence_tokens.remove(user_input)

        return robo_response



if __name__ == '__main__':
    vectorizer = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    data = get_corpus()

    sentence_tokens = []
    for d in data['data']:
        for token in d['sentence_tokens']:
            sentence_tokens.append(token)

    while True:
        user_input = str(input())
        user_input = user_input.lower()
        print("Chatbot: " + chatbot_response(user_input))
