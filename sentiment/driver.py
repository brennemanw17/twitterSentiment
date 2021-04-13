# Written by William Sam Brenneman
# CSCI 4130 @ ECU
import os
from sentiment.tokenizer import *
import csv

def run(docs, fname):
    temp = { }
    for doc in docs:
        filename = "preproccesed/analyzed" + doc
        doc = "data/" + doc
        with open(doc, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            for row in csv_reader:
                if row:
                    temp[row[0]] = porterstemmer(stopwordremover(tokenizer(row[1]),
                                                                 getstopwords("sentiment/stopwords.txt")))

    with open(fname, 'a', encoding="utf-8") as csvFile:
        csvWriter = csv.writer(csvFile)
        for key in temp:
            csvWriter.writerow([key, temp[key]])
    print("completed")





