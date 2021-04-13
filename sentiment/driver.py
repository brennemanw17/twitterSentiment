# Written by William Sam Brenneman
# CSCI 4130 @ ECU
import os
from sentiment.tokenizer import *
import csv
import json

def run(docs, fname):
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
        json.dump(temp, outfile)
    print("completed")

"""
    with open(fname, 'a', encoding="utf-8") as csvFile:
        csvWriter = csv.writer(csvFile)
        for key in temp:
            csvWriter.writerow([key, temp[key]])"""




def termFreq(doc):
    terms = { }
    with open(doc, 'r', encoding='utf-8') as json_file:
        json_reader = json.load(json_file)
        print(json_reader)

"""
        for row in json_reader:
            if row:
                temp = row[1]
                print(temp)
                print(temp[2])
                for word in temp:
                    if word in terms:
                        terms[word] = terms[word] + 1
                    else:
                        terms[word] = 1
    return terms"""



