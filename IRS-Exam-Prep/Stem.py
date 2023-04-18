from nltk.stem import PorterStemmer,LancasterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#from Stem import stemme
def stemme(wordarray,stemmer):
    stemmedwords = []
    if "ps" in stemmer:
        ps = PorterStemmer()
    # choose some words to be stemmed
        words = wordarray
        for w in words:
            stemmedwords.append(ps.stem(w))
    if "ls" in stemmer:
        ls = LancasterStemmer()
        # choose some words to be stemmed
        words = wordarray
        for w in words:
            stemmedwords.append(ls.stem(w))
    return stemmedwords


string = "thats the process of calculating the similarity"
df = string.split(" ")

x = stemme(df,"ps")
y = stemme(df,"ls")

print(x)
print(y)