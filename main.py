from tweetscraper.tweets import *

# how to call tweet scraper
# tweetScrape("$AMC", "2021-04-11", "0", 300)

from sentiment.driver import *

fbFiles = ["fb2021-04-11-11-10-03.csv","fb2021-04-11-11-35-10.csv", "fb2021-04-11-11-40-58.csv",
           "fb2021-04-11-11-41-24.csv", "fb2021-04-11-12-08-30.csv"]


run(fbFiles, "preproccesed/fb2021processed.json")

#termFreq("preproccesed/fb2021processed.json")