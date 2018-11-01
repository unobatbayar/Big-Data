"""
Amdahl's Law. Formula for Parallel Computing, quantify


Slatency is the theoretical speedup of the execution of the whole task;
s is the speedup of the part of the task that benefits from improved system resources;
p is the proportion of execution time that the part benefiting from improved resources originally occupied.

source: https://en.wikipedia.org/wiki/Amdahl%27s_law

It says, speedup we expect depends on two factors:
1) proportion of parallelism
2) number of processors

"""

speedup = 1/(1-p) + p/s

#and

{ speedup <= 1/(1-p)lim s-> ∞ speedup = 1/(1 - p)
