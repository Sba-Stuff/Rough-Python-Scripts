import math
df = input("Enter Document Frequency (Number of Documents Containing A Term): ")
N = input("Input Total Number of Documents: ")
idf = math.log10(int(N)/int(df))
print("Inverse Document Frequency = "+str(idf))