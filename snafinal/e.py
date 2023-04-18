import math
import sys

val1 = int(sys.argv[1])
val2 = int(sys.argv[2])
x = val1/val2
y = math.log2(val1/val2)
print(str(-x*y))
