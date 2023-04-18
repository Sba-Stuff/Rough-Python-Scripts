import sys

def stringtolist(str):
    din = []
    m = str.split(',')
    for f in m:
        din.append(f)
    return din

list1 = stringtolist(sys.argv[1])
list2 = stringtolist(sys.argv[2])
list1_as_set = set(list1)
intersection = list1_as_set.intersection(list2)
intersection_as_list = list(intersection)
print(intersection_as_list)