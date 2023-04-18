import math
import sys

val1 = int(sys.argv[1])
val2 = int(sys.argv[2])
val3 = int(sys.argv[3])
x = (val1/val3)**2
y = (val2/val3)**2
x1 = x+y
y1 = 1-x1

print(str(y1))
