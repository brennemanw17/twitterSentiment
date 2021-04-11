import apiconfig
import tweepy as tw
import time
import csv

auth = tw.OAuthHandler(apiconfig.consumer_key, apiconfig.consumer_secret)
auth.set_access_token(apiconfig.access_token, apiconfig.access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


keyword = "$fb"
keyname = keyword.replace('$', '')
keyname = keyname.replace(' ', '')
date = "2021-04-05"
timestmp = time.strftime("%Y-%m-%d-%H-%M-%S")
filename = "data/" + str(keyname + timestmp) + ".csv"

tweets = tw.Cursor(api.search, q=keyword, lang="en", since=date, until=date).items(300)

csvFile = open(filename, 'a', encoding="utf-8")
csvWriter = csv.writer(csvFile)
for tweet in tweets:
    csvWriter.writerow([tweet.created_at, tweet.text.replace('RT', '')])

print("Completed.")
