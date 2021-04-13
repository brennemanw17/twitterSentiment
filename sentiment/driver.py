# Written by William Sam Brenneman
# CSCI 4130 @ ECU

import os
from sentiment.tokenizer import *
import csv
import json


fbFiles = ["fb2021-04-11-11-10-03.csv", "fb2021-04-11-11-35-10.csv", "fb2021-04-11-11-40-58.csv",
           "fb2021-04-11-11-41-24.csv", "fb2021-04-11-12-08-30.csv"]
amznFiles = ["AMZN2021-04-11-11-42-47.csv", "AMZN2021-04-11-11-43-23.csv", "AMZN2021-04-11-11-43-39.csv",
             "AMZN2021-04-11-11-44-00.csv", "AMZN2021-04-11-12-10-23.csv"]
tslaFiles = ["TSLA2021-04-11-12-07-07.csv", "TSLA2021-04-11-12-07-23.csv", "TSLA2021-04-11-12-07-36.csv",
             "TSLA2021-04-11-12-07-51.csv", "TSLA2021-04-11-12-08-06.csv"]


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



