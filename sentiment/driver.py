# Written by William Sam Brenneman
# CSCI 4130 @ ECU
import os
from sentiment.tokenizer import *
import csv

def run(doc):
    temp = { }
    filename = "preproccesed/analyzed" + doc
    doc = "data/" + doc
    with open(doc, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            if row:
                temp[row[0]] = porterstemmer(stopwordremover(tokenizer(row[1]),
                                                             getstopwords("sentiment/stopwords.txt")))

    with open(filename, 'a', encoding="utf-8") as csvFile:
        csvWriter = csv.writer(csvFile)
        for key in temp:
            csvWriter.writerow([key, temp[key]])
    print("completed")



# documap reads all files in a given directory then
# uses the docuindex function to tokenize, stem and
# remove stopwords from each file read. After docuindex
# is used the returned dictionary is stored in another
# dictionary which holds all documents in the directory
def documap(directory):
    documapped = {}
    with os.scandir(directory) as files:
        for file in files:
            documapped[file.name] = docuindex(directory + "/" + file.name)
    return documapped



