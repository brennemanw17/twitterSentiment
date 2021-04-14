from tweetscraper.tweets import *

# tweetScrape("$AMC", "2021-04-11", "0", 300)

while True:
    print("Tweet Scraper \n 1) Scrape Tweets \n 2) Exit")
    input1 = int(input())
    if input1 == 1:
        print("Enter Search Term: ")
        searchterm = input()
        print("Enter Start Date (YYYY-MM-DD): ")
        fromdate = input()
        print("Enter end Date (YYYY-MM-DD or 0 for none): ")
        todate = input()
        print("Enter number of Tweets to scrape: ")
        tweetcount = int(input())
        tweetScrape(searchterm, fromdate, todate, tweetcount)
    elif input1 == 0:
        SystemExit
    else:
        print("Error unknown option")
