import json
from lxml import etree
import nltk
import re
import requests
import unidecode

url_wiki_us_presidents = 'https://en.wikipedia.org/wiki/List_of_Presidents_of_the_United_States'

XPATH_TEXT = "//div[@class='mw-parser-output']/p//text()"
XPATH_PRESIDENT_LINKS = "//table[@class='wikitable']/tbody/tr/td[4]/b/big/a/@href"

def make_request_with_xpath(url, xpath):
    response = requests.get(url)
    root = etree.HTML(response.content)
    raw_text = root.xpath(xpath)

    return raw_text

def get_wiki_urls():
    hrefs = make_request_with_xpath(url_wiki_us_presidents, XPATH_PRESIDENT_LINKS)
    wiki_urls = ['https://en.wikipedia.org' + suffix for suffix in hrefs]

    return wiki_urls

def raw_text_to_clean_string(raw_text):
    big_string = ''.join(raw_text).replace("\'","'")
    clean_string = unidecode.unidecode(re.sub('\[.+\]','',big_string))

    return clean_string

def parse_corpus(clean_string, url):
    sentence_tokens = nltk.sent_tokenize(clean_string)

    data = {
        'url': url,
        'sentence_tokens': sentence_tokens,
    }

    return data

if __name__ == '__main__':
    wiki_urls = get_wiki_urls()
    president_wikis = []

    for url in wiki_urls:
        print(url)

        try:
            raw_text = make_request_with_xpath(url=url, xpath=XPATH_TEXT)
            clean_string = raw_text_to_clean_string(raw_text)
            data = parse_corpus(clean_string=clean_string, url=url)
            president_wikis.append(data)
        except Exception as e:
            print(e)

    total_data = {'data': president_wikis}

    with open('data/presidents.json', 'w') as outfile:
        json.dump(total_data, outfile)
