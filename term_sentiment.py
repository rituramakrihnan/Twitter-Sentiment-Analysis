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


# Read the tweet_file. Extract each tweet per line. Append to the tweet_data list.
def read_tweet_file(tweet_file):
    tweet_data = []
    tweet_objects = []

    try:
        tweet_objects = json.load(tweet_file)
    except:
        tweet_file = open(sys.argv[2])
        for line in tweet_file:
            jsonline = json.loads(line)
            tweet_objects.append(jsonline)

    for tweetObject in tweet_objects:
        try:
            tweet_data.append(tweetObject["text"])
        except:
            continue
    return tweet_data


# filtering the tweets
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


# computing the tweet sentiment for the tweets
def compute_tweet_sentiment(td, sc):
    sentiments = []
    for t in td:
        sentiment = 0.0
        words = filter_tweet(t)
        # Derive sentiment from each tweet by summing up sentiments of individual words.
        for w in words:
            if w in sc:
                sentiment = sentiment + sc[w]
        sentiments.append(sentiment)
        # print('words'+str(words)+'Sentiments'+str(sentiments))
    return sentiments


# computing the term sentiment for the tweets
def compute_term_sentiment(td, sc, ts):
    idx = 0
    occur = {}

    for t in td:
        words = filter_tweet(t)
        for w in words:
            occur[w] = 0
    finalW = {}
    for t in td:
        words = filter_tweet(t)
        for w in words:
            occur[w] = occur[w] + 1
            if w not in sc:
                sc[w] = ts[idx]
            else:
                sc[w] = (sc[w] + ts[idx]) / occur[w]  # take the average
            finalW[w] = sc[w]
        idx = idx + 1
    for w in finalW:
        print(str(w) + "   " + '%0.3f' % finalW[w])
    return sc


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = dict_from_sentiment_file(sent_file)
    tweet_data = read_tweet_file(tweet_file)
    tweet_sentiments = compute_tweet_sentiment(tweet_data, scores)
    compute_term_sentiment(tweet_data, scores, tweet_sentiments)


if __name__ == '__main__':
    main()
