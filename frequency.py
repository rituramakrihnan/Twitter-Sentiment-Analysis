import sys
import json
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords


def hw():
    print('Hello, world!')


def lines(fp):
    print(str(len(fp.readlines())))


def main():
    tweet_file = open(sys.argv[1])
    # Read the tweet file
    tweet_data = []
    tweet_objects = []

    try:
        tweet_objects = json.load(tweet_file)
    except:
        tweet_file = open(sys.argv[1])
        for line in tweet_file:
            jsonline = json.loads(line)
            tweet_objects.append(jsonline)

    for tweet_object in tweet_objects:
        try:
            tweet_data.append(tweet_object["text"])
        except:
            continue
    # For each tweet
    occur = {}
    for t in tweet_data:
        total = 0
        # Encoding it into UTF-8
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

        for w in words_cleaned:
            if w not in occur:
                occur[w] = 1
            else:
                occur[w] = occur[w] + 1
            # print(occur)

    for w in occur.keys():
        print(f"{str(w)}  {occur[w]}")


if __name__ == '__main__':
    main()
