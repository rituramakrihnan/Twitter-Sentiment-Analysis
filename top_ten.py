import json
from collections import Counter
import sys


def hw():
    print('Hello, world!')


def lines(fp):
    print(str(len(fp.readlines())))


def main():
    tweet_file = open(sys.argv[1])
    # Read the tweet file
    tweet_objects = []

    try:
        tweet_objects = json.load(tweet_file)
    except:
        tweet_file = open(sys.argv[1])
        for line in tweet_file:
            jsonline = json.loads(line)
            tweet_objects.append(jsonline)

    # Create an empty list to store all hashtags
    hashtags = []

    # Loop through each tweet in the data
    for tweet in tweet_objects:
        # Extract the hashtags from the tweet
        tags = tweet['entities']['hashtags']
        # Loop through each hashtag and append it to the list of all hashtags
        for tag in tags:
            hashtags.append(tag['text'])

    # Use Counter to count the frequency of each hashtag
    freq = Counter(hashtags)

    # Get the top ten hashtags
    top_ten = freq.most_common(10)

    # Print the top ten hashtags
    print('Top ten hashtags:')
    for tag, count in top_ten:
        print(tag, count)


if __name__ == '__main__':
    main()
