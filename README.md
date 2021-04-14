# Twitter Sentinment Analysis -- CSCI 4130
Topic based Tweet collection and sentiment analysis

## Requirements: 
pip3 install nltk

pip3 install tweepy

Python 3 



## Functionality:
The functionality of our implementation is to: 
1) Collect dataset from twitter regarding Amazon, Tesla, and Facebook stocks 

2) Preprocess the data (Stop-word removal, tokenize, normalization)

3) Match tweets from our dataset against the vocabulary to measure accuracy

4) Measure accuracy scores based on precision and recall


## Running:

##### TweetScraper:
To run the tweetScraper use:
```
python3 scrapeTweets.py
```
From there you will be prompted to fill out the needed information. Once done the scraper will print "completed" and your scraped tweets will be saved in the data directory.
