import math
tf = input("Enter Term Frequency: ")
ltf1 = math.log10(int(tf))
ltf2 = 1+ltf1
print("Log Term Frequency = "+str(ltf2))