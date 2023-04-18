import math
import sys

val1 = int(sys.argv[1])
val2 = int(sys.argv[2])
val3 = int(sys.argv[3])
x = val1/val3
y = math.log2(val1/val3)
x1 = val2/val3
y1 = math.log2(val2/val3)

print(str(-x*y-x1*y1))
