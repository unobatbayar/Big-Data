"""Lab 3. Working with Tweets
"""
from mrjob.job import MRJob
import re
# WORK NEEDS TO BE DONE + REVISION
#this is a regular expression that finds all the words inside a String
WORD_REGEX = re.compile(r"\b\w+\b")

#This line declares the class, that extends the MRJob format.
class Quiz2(MRJob):
    def mapper(self, _, line):
        try:
            fields = line.split(';')
            if len(fields) == 4 :
                bin = 5*math.floor(int(len(fields[2]))/5)
                yield (bin, 1)
        except:
            pass
            #do nothing
    def reducer(self, bin, counts):
        yield (bin, sum(counts))


if __name__ == '__main__':
    Quiz2.run()
