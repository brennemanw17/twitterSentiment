from sentiment.driver import *

"""
fbFiles = ["fb2021-04-11-11-10-03.csv", "fb2021-04-11-11-35-10.csv", "fb2021-04-11-11-40-58.csv",
           "fb2021-04-11-11-41-24.csv", "fb2021-04-11-12-08-30.csv"]
amznFiles = ["AMZN2021-04-11-11-42-47.csv", "AMZN2021-04-11-11-43-23.csv", "AMZN2021-04-11-11-43-39.csv",
             "AMZN2021-04-11-11-44-00.csv", "AMZN2021-04-11-12-10-23.csv"]
tslaFiles = ["TSLA2021-04-11-12-07-07.csv", "TSLA2021-04-11-12-07-23.csv", "TSLA2021-04-11-12-07-36.csv",
             "TSLA2021-04-11-12-07-51.csv", "TSLA2021-04-11-12-08-06.csv"]
"""

# ------------- Example function calls

# --- how to call tweet scraper
# tweetScrape("$AMC", "2021-04-11", "0", 300)

# print(termfreq("preproccesed/fb2021processed.json"))

# amznSet = dataSet(amznFiles)
# fbSet = dataSet(fbFiles)
# tslaSet = dataSet(tslaFiles)

# dataSets = [amznSet, fbSet, tslaSet]
# print(positiveSet.vocab)


# Test data set placeholder
testData = dataSet(["947-negatives.csv"])


# --- Analysis functions

# Converts the training CSV's into a usable format for our program
def vocabtolist():
    terms = []
    positiveSet = dataSet(["positive-Sentiment.csv"])
    negativeSet = dataSet(["negative-Sentiment.csv"])

    for key in positiveSet.vocab:
        tup = (key, "positive")
        terms.append(tup)

    for key in negativeSet.vocab:
        tup = (key, "negative")
        terms.append(tup)

    return terms


# Converts json files to a list object
def jsontolist(doc):
    terms = []
    with open(doc, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for key in data:
            if len(data[key]) > 0:
                terms.append(data[key])
    return terms


trainingSet = vocabtolist()

# Various Test Data Sets

# testSet = jsontolist("preproccesed/fb2021processed.json")
# testSet = jsontolist("preproccesed/AMZN2021processed.json")
# testSet = jsontolist("preproccesed/TSLA2021processed.json")
testSet = jsontolist("preproccesed/947processed.json")


# ------------------------------------------------------------------------------------------------------------------------------


# Builds a word bank that contains every work in the training set given to it
def buildVocabList(trainingSetData):
    all_words = []

    for words in trainingSetData:
        all_words.append(words[0])

    wordlist = nltk.FreqDist(all_words)
    word_features1 = wordlist.keys()

    # print(word_features1)

    return word_features1


# ------------------------------------------------------------------------------------------------------------------------------

# Compares each word in the word bank (word_features) and gives it a label: either true or false, where true means
# word is in the tweet and false means it is absent
def getfeatures(tweet):
    tweet_words = set(tweet)
    features = {}

    for word in word_features:
        features['contains(%s)' % word] = (word in tweet_words)

    # print(features)

    return features


# ----------------------------------------------------------------------------------------------------------------------------

# Builds the vocabulary list
print("Building vocabulary bank..")
word_features = buildVocabList(trainingSet)
# print(word_features)


# Classifies features within the training set
print("Classifying features..")
trainingFeatures = nltk.classify.apply_features(getfeatures, trainingSet)

# Trains the model based on the features
print("Training Data..")
NBayesClassifier = nltk.NaiveBayesClassifier.train(trainingFeatures)

print("Results:")
NBResultsLabels = [NBayesClassifier.classify(getfeatures(tweet[0])) for tweet in testSet]

print(NBResultsLabels)
print("")

# Prints the positive/negative sentiment depending on however many postive/negative tweets there are out of the
# total number of tweets
if NBResultsLabels.count('positive') > NBResultsLabels.count('negative'):
    print("Positive Sentiment" + str(100 * NBResultsLabels.count('positive') / len(NBResultsLabels)) + "%")
else:
    print("Negative Sentiment " + str(100 * NBResultsLabels.count('negative') / len(NBResultsLabels)) + "%")
