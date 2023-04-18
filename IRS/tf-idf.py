import math
tf = float(input("Term Frequency: "))
idf = float(input("Inverse Document Frequency: "))
tfidf = tf*idf
print(str(tfidf))