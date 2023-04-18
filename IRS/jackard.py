from jacardsupport import merge,stringtolist,removeduplicate,intersect
from math import sqrt

input_query = input("Enter Query: ")
output_query = input("Document Text: ")

list1 = stringtolist(input_query)
list2 = stringtolist(output_query)
if len(list1)==len(list2):
	print("Jackard Do Not Work On Same Query And Text Size Documents")
merged_output = merge(list1,list2)
union = removeduplicate(merged_output)
intersection = intersect(list1,list2)
print("----------------------------")
print("Union")
print(" ")
print(union)
print("----------------------------")
print("Intersection")
print(" ")
print(intersection)
print("----------------------------")
print(" ")
jackard = len(intersection)/len(union)
print("Jackard")
print(jackard)
print(" ")
print("----------------------------")
print("Normalized Jackard")
njackard = len(intersection)/sqrt(len(union))
print(njackard)