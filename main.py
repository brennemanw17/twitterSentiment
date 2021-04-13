from tweetscraper.tweets import *
import nltk
from sentiment.driver import *

# ------------- TEST SETS
positiveSet = dataSet(["positive-Sentiment.csv"])
negativeSet = dataSet(["negative-Sentiment.csv"])

fbFiles = ["fb2021-04-11-11-10-03.csv", "fb2021-04-11-11-35-10.csv", "fb2021-04-11-11-40-58.csv",
           "fb2021-04-11-11-41-24.csv", "fb2021-04-11-12-08-30.csv"]
amznFiles = ["AMZN2021-04-11-11-42-47.csv", "AMZN2021-04-11-11-43-23.csv", "AMZN2021-04-11-11-43-39.csv",
             "AMZN2021-04-11-11-44-00.csv", "AMZN2021-04-11-12-10-23.csv"]
tslaFiles = ["TSLA2021-04-11-12-07-07.csv", "TSLA2021-04-11-12-07-23.csv", "TSLA2021-04-11-12-07-36.csv",
             "TSLA2021-04-11-12-07-51.csv", "TSLA2021-04-11-12-08-06.csv"]

# ------------- Example function calls

# --- how to call tweet scraper
# tweetScrape("$AMC", "2021-04-11", "0", 300)


# --- Analysis functions

tweetProcessor = dataSet(fbFiles)

preprocessedTrainingSet = tweetProcessor.__init__(fbFiles)
preprocessedTestSet = tweetProcessor.__init__(positiveSet)


# process(fbFiles, "preproccesed/fb2021processed.json")


# print(termfreq("preproccesed/fb2021processed.json"))

# amznSet = dataSet(amznFiles)
# fbSet = dataSet(fbFiles)
# tslaSet = dataSet(tslaFiles)

# dataSets = [amznSet, fbSet, tslaSet]

# print(positiveSet.vocab)


def buildVocabList(processedTrainingData):
    all_words = []

    for (words, sentiment) in processedTrainingData:
        all_words.extend(words)

    wordlist = nltk.FreqDist(all_words)
    word_features = wordlist.keys()

    return word_features


def getfeatures(tweet):
    tweet_words = set(tweet)
    features = {}

    for word in word_features:
        features['contains(%s)' % word] = (word in tweet_words)

    return features

print("Building vocabulary.")
word_features = buildVocabList(preprocessedTrainingSet)

print("Classifying features.")
trainingFeatures = nltk.classify.apply_features(getfeatures(preprocessedTrainingSet))

print("Running Data on Naive Bayes Classifier")
NBayesClassifier = nltk.NaiveBayesClassifier.train(trainingFeatures)

print("Results")
NBResultsLabels = [NBayesClassifier.classify(getfeatures(tweet[0])) for tweet in preprocessedTestSet]

print(NBResultsLabels)
print("")

if NBResultsLabels.count('positive') > NBResultsLabels.count('negative'):
    print("NB Result Positive Sentiment " + str(100 * NBResultsLabels.count('positive') / len(NBResultsLabels))+"%")
else:
    print("NB Result Negative Sentiment " + str(100 * NBResultsLabels.count('negative') / len(NBResultsLabels))+"%")