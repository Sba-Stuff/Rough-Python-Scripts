import math
import sys
import statistics


i = float(input("Enter X1: "))
j = float(input("Enter Y1: "))

k = float(input("Enter X2: "))
l = float(input("Enter Y2: "))

x1minx2 = i-k
y1miny2 = j-l

val1 = x1minx2*x1minx2
val2 = y1miny2*y1miny2

print(str(math.sqrt(val1+val2)))