import sys
import json
import re

import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords


# Read the sentiment_file, and build a dictionary of terms and their scores.
def dict_from_sentiment_file(sf):
    scores = {}
    for line in sf:
        term, score = line.split('\t')
        scores[term] = int(score)
    return scores


def filter_tweet(t):
    encoded_t = t.encode('utf-8').decode("utf-8").lower()
    encoded_words = encoded_t.split()
    # print('encoded'+str(encoded_words))
    for w in encoded_words:
        if w.startswith('www') or w.startswith('http'):
            # print(w)
            encoded_words.remove(w)

    # Filtered out non alpha-numeric characters, including @, punctuations.
    pattern = re.compile('[^A-Za-z]+')
    words = [pattern.sub("", w) for w in encoded_words]  # Sans lambda

    for word in words:
        if "" == word:
            words.remove(word)

    words_cleaned = []
    stop_words = set(stopwords.words('english'))
    for word in words:
        if word not in stop_words:
            words_cleaned.append(word)
    return words_cleaned


# computing the tweet sentiment for a tweet
def compute_tweet_sentiment(td, sc):
    sentiment = 0.0
    words = filter_tweet(td)
    # Derive sentiment from each tweet by summing up sentiments of individual words.
    for w in words:
        if w in sc:
            sentiment = int(sentiment) + int(sc[w])
    return sentiment


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = dict_from_sentiment_file(sent_file)
    count = {}
    max_value = -10000
    happiest = ""
    tweet_objects = []

    try:
        tweet_objects = json.load(tweet_file)
    except:
        tweet_file = open(sys.argv[2])
        for line in tweet_file:
            jsonline = json.loads(line)
            tweet_objects.append(jsonline)

    # tweet_objects = json.load(tweet_file)

    for tweets in tweet_objects:
        if tweets.get('place') is not None:
            if (tweets['place']['country_code'] == 'US') & (tweets['place']['place_type'] == 'city'):
                state = (tweets['place']['full_name'].split(',')[1]).strip()
                if "text" in tweets.keys():
                    sent = compute_tweet_sentiment(tweets["text"], scores)
                    if state in count:
                        count[state] = count[state] + sent
                    else:
                        count[state] = sent
    for s in count.keys():
        if count[s] > max_value:
            max_value = count[s]
            happiest = s

    print(happiest)


if __name__ == '__main__':
    main()
