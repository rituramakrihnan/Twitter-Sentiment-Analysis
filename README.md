# Twitter-Sentiment-Analysis
## Files

### Python Files
1. `scrapper.py`
2. `tweet_sentiment.py`
3. `term_sentiment.py`
4. `frequency.py`
5. `happiest_state.py`
6. `top_ten.py`

### Input Files
1. `tweets_data.json` (generated tweets in JSON format)
2. `data.json` (file provided)
3. `positive_tweets_data.json` (online data to test term sentiment)
4. `negative_tweets_data.json` (online data to test term sentiment)

### Output Files
1. `Output_tweets_sentiment.txt`
2. `Output_term_sentiment.txt`
3. `Output_frequency.txt`
4. `Output_Happiest_State.txt`
5. `Output_Top_Ten.txt`

## Problems and Solutions

### Problem 1: Get Twitter Data

**Solution:**  
The `scrapper.py` file generates the tweets in JSON format. Update the Twitter credentials in the file:

```python
# credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_TOKEN_SECRET"
```

The tweets are collected and stored in the `tweets_data.json` file.

### Problem 2: Derive the Sentiment of Each Tweet

**Solution:**  
Run the following command:
```bash
$ python tweet_sentiment.py AFINN-111.txt tweets_data.json
```

The tweet_sentiment.py file generates sentiment for the words in the AFINN-111.txt file.
The output is available in the Output_tweets_sentiment.txt file.

### Problem 3: Derive the Sentiment of New Terms

**Solution:**  

Run the following command:
```python
$ python term_sentiment.py AFINN-111.txt tweets_data.json
```

The term_sentiment.py file generates sentiments for terms not in the AFINN-111.txt. Stop words and numerical values are eliminated. For testing, positive_tweets_data.json and negative_tweets_data.json are used.
The output is available in the Output_term_sentiment.txt file.

### Problem 4: Compute Term Frequency

**Solution:**  

Run the following command:
```python
$ python frequency.py tweets_data.json
```

The frequency.py file computes term frequency.
The output is available in the Output_frequency.txt file.

### Problem 5: Which State is the Happiest?

**Solution:** 

Run the following command:
```python
$ python happiest_state.py AFINN-111.txt tweets_data.json
```

The happiest_state.py file calculates the happiest state based on tweets containing the state's name.
The output is available in the Output_Happiest_State.txt file.

### Problem 6: Top Ten Hashtags

**Solution:** 

Run the following command:
```python
$ python top_ten.py tweets_data.json
```

The top_ten.py file computes the ten most frequently occurring hashtags from the data.
The output is available in the Output_Top_Ten.txt file.
