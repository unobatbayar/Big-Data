"""Lab 1. Basic wordcount
@author uno
"""
from mrjob.job import MRJob
import re

#this is a regular expression that finds all the words inside a String
WORD_REGEX = re.compile(r"\b\w+\b")

#This line declares the class, that extends the MRJob format.
class wordcount(MRJob):

# this class will define two additional methods: the mapper method goes here
    def mapper(self, _, line):
        words = WORD_REGEX.findall(line)
        for word in words:
            yield (word.lower(), 1)

#and the reducer method goes after this line
    def reducer(self, word, counts):
        yield word, (sum(counts))

if __name__ == '__main__':
    wordcount.run()
