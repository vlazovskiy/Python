import collections

file = open("") #Filename goes here

stopwords = set(line.strip() for line in open('')) #Stopwords .txt file goes here
#Stopwords can be found here [stopwords](stopwords.md)

wordcount = {}

for word in file.read().lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace("\"", "")
    word = word.replace("“", "")
    if word not in stopwords: 
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
        
d = collections.Counter(wordcount)

for word, count in d.most_common(10):
    print(word, ":", count)
