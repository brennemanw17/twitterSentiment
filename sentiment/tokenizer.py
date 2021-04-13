# Written by William Sam Brenneman
# CSCI 4130 @ ECU
import re
from nltk.stem import PorterStemmer


# Takes in string msg, then creates a list containing
# all words in the string excluding all spaces, punctuation and numbers.
def tokenizer(msg):
    msg = msg.lower()
    msg = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', msg)  # remove URL
    msg = re.sub('@[^\s]+', 'AT_USER', msg)  # remove usernames
    msg = re.sub(r'#([^\s]+)', r'\1', msg)  # remove #
    word = ""
    wordlist = []
    for char in msg:
        if char.isalpha():
            word = word + char
        elif (char == " " or char == "-" or char == "/") and word.isalpha():
            wordlist.append(word)
            word = ""
    if word != " " and word != "":
        wordlist.append(word)
    return wordlist


# opens file with given filename, then reads file line by line
# putting each line into a list and returning that list
# strips spaces
def getstopwords(filename):
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
    return lines

# stopwordremover has two parameters
# list: list of words
# stopwords: list of stopwords
# stopwordremover removes stopwords in stopwords list from words
# in the word list, list.
def stopwordremover(list, stopwords):
    newlist = []
    for x in list:
        if x not in stopwords:
            newlist.append(x)
    return newlist


# porterstemmer uses NLTK's Porter stemmer function to stem each word in
# the list List
# list: list of english words to stem
# returns: stemmed words from list
def porterstemmer(list):
    ps = PorterStemmer()
    newlist = []
    for x in list:
        newlist.append(ps.stem(x))
    return newlist

