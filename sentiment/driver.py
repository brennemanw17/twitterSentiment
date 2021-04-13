# Written by William Sam Brenneman
# CSCI 4130 @ ECU

import os
from sentiment.tokenizer import *
import csv
import json


def processtweets(docs, fname):
    temp = { }
    for doc in docs:
        filename = "preproccesed/analyzed" + doc + ".json"
        doc = "data/" + doc
        with open(doc, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                if row:
                    temp[row[0]] = porterstemmer(stopwordremover(tokenizer(row[1]),
                                                                 getstopwords("sentiment/stopwords.txt")))
    with open(fname, "w", encoding="utf-8") as outfile:
        json.dump(temp, outfile, indent=4)
    print("completed")


def termfreq(doc):
    terms = { }
    with open(doc, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

        for key in data:
            for word in data[key]:
                if word in terms:
                    terms[word] = terms[word]+1
                else:
                    terms[word] = 1
    return terms


class dataSet:
    def __init__(self, filenames):
        self.filenames = filenames
        self.processedName = "preproccesed/" + filenames[0].partition("-")[0] + "processed.json"

        processtweets(self.filenames, self.processedName)

        self.vocab = termfreq(self.processedName)



