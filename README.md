# US President Chatbot

This chatbot answers your questions about US presidents using data from their Wikipedia pages.

Under the hood, this chatbot returns the sentence in the entire corpus of wikipedia sentences about US presidents that is nearest to the text entered by the user - ranked by cosine similarity of the term frequency inverse document frequency of the user text and each sentence in the corpus.

For example:

Q: 'Where was Obama born?'
Chatbot: Obama was born in Honolulu, Hawaii.

Q: 'Where did Obama go to law school?'
Chatbot: In 1988, he enrolled in Harvard Law School, where he was the first black president of the Harvard Law Review.

Q: 'Who is the vice president for Donald Trump?'
Chatbot: The contenders included even Donald Trump, who had previously been skeptical.

### Getting Started

First, run the `get_corpus.py` program to scrape and save as json data the text from the wikipedia page for every US president.

To launch the chatbot, simply run the `chatbot.py` program.

To interact with the chatbot, enter text into the command line, surrounded by single quote marks, like this:

```
'Where was Obama born?'
```
