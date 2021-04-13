from tweetscraper.tweets import *

# how to call tweet scraper
# tweetScrape("$AMC", "2021-04-11", "0", 300)

from sentiment.driver import *

# ------------- TEST SETS
positiveSet = dataSet(["positiveSentiment.csv"])
negativeSet = dataSet(["negativeSentiment.csv"])

fbFiles = ["fb2021-04-11-11-10-03.csv", "fb2021-04-11-11-35-10.csv", "fb2021-04-11-11-40-58.csv",
           "fb2021-04-11-11-41-24.csv", "fb2021-04-11-12-08-30.csv"]
amznFiles = ["AMZN2021-04-11-11-42-47.csv", "AMZN2021-04-11-11-43-23.csv", "AMZN2021-04-11-11-43-39.csv",
             "AMZN2021-04-11-11-44-00.csv", "AMZN2021-04-11-12-10-23.csv"]
tslaFiles = ["TSLA2021-04-11-12-07-07.csv", "TSLA2021-04-11-12-07-23.csv", "TSLA2021-04-11-12-07-36.csv",
             "TSLA2021-04-11-12-07-51.csv", "TSLA2021-04-11-12-08-06.csv"]

# ------------- Example function calls

# process(fbFiles, "preproccesed/fb2021processed.json")

# print(termfreq("preproccesed/fb2021processed.json"))

# amznSet = dataSet(amznFiles)
# fbSet = dataSet(fbFiles)
# tslaSet = dataSet(tslaFiles)

# dataSets = [amznSet, fbSet, tslaSet]

# print(positiveSet.vocab)
