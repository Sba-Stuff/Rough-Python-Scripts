def stringtolist(str):
    din = []
    m = str.split(' ')
    for f in m:
        din.append(f)
    return din

def removeduplicate(list):
    final_list = []
    for value in list:
        if value not in final_list:
            final_list.append(value)
    return final_list

def merge(list1,list2):
     fl = []
     for m in list1:
         fl.append(m)
     for n in list2:
         fl.append(n)
     return fl

def intersect(list1,list2):
	list1_as_set = set(list1)
	intersection = list1_as_set.intersection(list2)
	intersection_as_list = list(intersection)
	return intersection_as_list