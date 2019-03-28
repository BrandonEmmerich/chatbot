import json
from lxml import etree
import nltk
import re
import requests
import unidecode

url_wiki_obama = 'https://en.wikipedia.org/wiki/Barack_Obama'

XPATH_TEXT = "//div[@class='mw-parser-output']/p//text()"


def make_request_with_xpath(url, xpath):
    response = requests.get(url)
    root = etree.HTML(response.content)
    content = root.xpath(xpath)

    return content

def clean_string(raw_text):
    big_string = ''.join(raw_text).replace("\'","'")
    clean_string = unidecode.unidecode(re.sub('\[.+\]','',big_string))

    return clean_string

def parse_corpus(clean_string):
    sentence_tokens = nltk.sent_tokenize(clean_string)
    word_tokens = nltk.word_tokenize(clean_string)

    data = {
        'sentence_tokens': sentence_tokens,
        'word_tokens': word_tokens,
    }

    return data

if __name__ == '__main__':
    raw_text = make_request_with_xpath(url_wiki_obama, XPATH_TEXT)
    clean_string = clean_string(raw_text)
    data = parse_corpus(clean_string)

    with open('data/obama.json', 'w') as outfile:
        json.dump(data, outfile)
