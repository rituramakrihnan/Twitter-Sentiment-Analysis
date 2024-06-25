import sys
import json
import re


def hw():
    print('Hello, world!')


def lines(fp):
    print(str(len(fp.readlines())))


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    # Reading the sentiment file and building a dictionary
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    # Read the tweet file
    tweet_data = []
    tweet_objects = []

    try:
        tweet_objects = json.load(tweet_file)
    except:
        tweet_file = open(sys.argv[2])
        for line in tweet_file:
            jsonline = json.loads(line)
            tweet_objects.append(jsonline)

    for tweet_object in tweet_objects:
        try:
            tweet_data.append(tweet_object["text"])
        except:
            continue
    # print(tweet_data)

    # For each tweet
    for t in tweet_data:
        total = 0
        # Encoding it into UTF-8
        encoded_t = t.encode('utf-8').decode("utf-8")
        encoded_words = encoded_t.split()
        # print('encoded'+str(encoded_words))
        for w in encoded_words:
            if w.startswith('www') or w.startswith('http'):
                encoded_words.remove(w)

        # Filtered out non alpha-numeric characters, including @, punctuations.
        pattern = re.compile('[^A-Za-z]+')
        words = [pattern.sub("", w) for w in encoded_words]  # Sans lambda

        for word in words:
            if "" == word:
                words.remove(word)
        # print(words)

        # Sum up the sentiment of words in a tweet.
        for w in words:
            if w in scores:
                # print(t+': '+w+' '+str(scores[w]))
                total = total + scores[w]

        print('%0.2f' % total)


if __name__ == '__main__':
    main()
