from tweetscraper.tweets import *
import nltk
from sentiment.driver import *

# ------------- TEST SETS
positiveSet = ["positive-Sentiment.csv"]
negativeSet = ["negative-Sentiment.csv"]

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

def jsontolist(doc):
    terms = []
    with open(doc, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for key in data:
            terms.append(data[key])
    return terms


trainingSet = [('good', 'positive'), ('dip', 'negative')]
# "positiveprocessed.json"

testSet = jsontolist("preproccesed/fb2021processed.json")


# print(termfreq("preproccesed/fb2021processed.json"))

# amznSet = dataSet(amznFiles)
# fbSet = dataSet(fbFiles)
# tslaSet = dataSet(tslaFiles)

# dataSets = [amznSet, fbSet, tslaSet]

# print(positiveSet.vocab)

# ------------------------------------------------------------------------------------------------------------------------------

def buildVocabList(trainingSet):
    all_words = []

    for words in trainingSet:
        all_words.extend(words)

    wordlist = nltk.FreqDist(all_words)
    word_features = wordlist.keys()

    return word_features


# ------------------------------------------------------------------------------------------------------------------------------

def getfeatures(tweet):
    tweet_words = set(tweet)
    features = {}

    for word in word_features:
        features['contains(%s)' % word] = (word in tweet_words)

    return features


# ----------------------------------------------------------------------------------------------------------------------------


print("Building vocabulary.")
word_features = buildVocabList(trainingSet)
print(word_features)

print("Classifying features.")
trainingFeatures = nltk.classify.apply_features(getfeatures, trainingSet)



print("Running Data on Naive Bayes Classifier:")
NBayesClassifier = nltk.NaiveBayesClassifier.train(trainingFeatures)



print("Results")
NBResultsLabels = [NBayesClassifier.classify(getfeatures(tweet)) for tweet in testSet]

print(NBResultsLabels)
print("")

if NBResultsLabels.count('positive') > NBResultsLabels.count('negative'):
    print("NB Result Positive Sentiment " + str(100 * NBResultsLabels.count('positive') / len(NBResultsLabels)) + "%")
else:
    print("NB Result Negative Sentiment " + str(100 * NBResultsLabels.count('negative') / len(NBResultsLabels)) + "%")

