#   Twitter Tweet scraper Written by William S Brenneman
#   https://github.com/brennemanw17

import tweetscraper.apiconfig
import tweepy as tw
import time
import csv

auth = tw.OAuthHandler(tweetscraper.apiconfig.consumer_key, tweetscraper.apiconfig.consumer_secret)
auth.set_access_token(tweetscraper.apiconfig.access_token, tweetscraper.apiconfig.access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

def tweetScrape(keyword, dfrom, dto, amount):
    keyname = keyword.replace('$', '')
    keyname = keyname.replace(' ', '')
    timestmp = time.strftime("%Y-%m-%d-%H-%M-%S")
    filename = "data/" + str(keyname + timestmp) + ".csv"

    if dto == "0":
        tweets = tw.Cursor(api.search, q=keyword, lang="en", since=dfrom).items(amount)
    else:
        tweets = tw.Cursor(api.search, q=keyword, lang="en", since=dfrom, until=dto).items(amount)

    csvFile = open(filename, 'a', encoding="utf-8")
    csvWriter = csv.writer(csvFile)
    for tweet in tweets:
        csvWriter.writerow([tweet.created_at, tweet.text.replace('RT', '')])

    print("Completed.")
