import sys
import math
x = int(sys.argv[1])
z = int(sys.argv[2])
s = math.log2(x/z)
a = x/z
print(str(-1*s*a))
