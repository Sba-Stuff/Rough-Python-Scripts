import math
import sys
sum = 0
val1 = sys.argv[1]
val2 = val1.split(',')
for vf in val2:
     sum = sum+int(vf)
n = len(val2)
avg = (sum)/n
print(str(avg))