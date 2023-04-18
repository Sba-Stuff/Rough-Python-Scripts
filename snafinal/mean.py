import math
import sys
import statistics

val1 = str(sys.argv[1])
n = val1.split(',')
mean = 0
n_count= len(n)
for x in n:
        mean = mean + float(x)/n_count
print("Mean: "+str(mean))

sample = []
for f in n:
    sample.append(float(f))
print("Standard Deviation: "+str(statistics.stdev(sample)))