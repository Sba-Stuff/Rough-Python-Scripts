import sys
import math

def stringtolist(str):
    din = []
    m = str.split(',')
    for f in m:
        din.append(f)
    return din
def sum_of_list(list1):
	sum = 0
	for fio in list1:
		sum = sum+int(fio)
	return sum
def sum_of_square(list):
	summer=[]
	for c in list:
		x = int(c)*int(c)
		summer.append(str(x))
	return summer
list1 = stringtolist(sys.argv[1])
xco = math.sqrt(sum_of_list(sum_of_square(list1)))
print(str(xco))