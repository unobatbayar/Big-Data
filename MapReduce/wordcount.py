"""Lab 1. Basic wordcount using MapReduce 
"""
from mrjob.job import MRJob
import re

#this is a regular expression that finds all the words inside a String
WORD_REGEX = re.compile(r"\b\w+\b")

#This line declares the class, that extends the MRJob format.
class Lab1(MRJob):

# this class will define two additional methods: the mapper method goes here
    def mapper(self, _, line):
        words = WORD_REGEX.findall(line)
        for word in words:
            yield (word.lower(), 1)

#and the reducer method goes after this line
#added, now only shows words that appear 10 or more times
    def reducer(self, word, counts):
        summ = (sum(counts))
        if summ >= 10:
            yield word, (summ)

if __name__ == '__main__':
    Lab1.run()
