# Written by William Sam Brenneman
# CSCI 4130 @ ECU

import csv
import json
import nltk

from sentiment.tokenizer import *


# PreProcceses tweets contained in given list of documents docs
# saves preprocessed tweets to a single json file with the name fname
def processtweets(docs, fname):
    temp = {}
    for doc in docs:
        filename = "preproccesed/analyzed" + doc + ".json"
        doc = "data/" + doc
        with open(doc, 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                if row:
                    temp[row[0]] = stopwordremover(tokenizer(row[1]), getstopwords("sentiment/stopwords.txt"))
                    i = 2
                    try:
                        while row[i]:
                            temp[row[0]] = temp[row[0]] + stopwordremover(tokenizer(row[i]), getstopwords("sentiment/stopwords.txt"))
                            i = i+1
                    except IndexError:
                        pass

    with open(fname, "w", encoding="utf-8") as outfile:
        json.dump(temp, outfile, indent=4)
    print("completed process tweets")


# Reads all words in given docs and produces frequency distrobution
def termfreq(doc):
    terms = {}
    with open(doc, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

        for key in data:
            for word in data[key]:
                if word in terms:
                    terms[word] = terms[word] + 1
                else:
                    terms[word] = 1
    return terms


# dataSet represents one set of data (ie one processed json file)
# dataSet is initialized with a list of docs then calling processtweets
# to compile and preprocess all the docs into one json file then calls termfreq
class dataSet:
    def __init__(self, filenames):
        self.filenames = filenames
        self.processedName = "preproccesed/" + filenames[0].partition("-")[0] + "processed.json"

        processtweets(self.filenames, self.processedName)

        self.vocab = termfreq(self.processedName)



"""
def load(directory):
    documapped = {}
    with os.scandir(directory) as files:
        for file in files:
            temp = file.name.partition("-")[0]
            if temp in documapped:
                documapped[temp].append(file.name)
            else:
                documapped[temp] = [file.name]
    return documapped"""
