# Find the most common word

import re
from collections import Counter

N = 10  #specify the first N most occurring words

file = input('file: ')

words = re.findall(r'\w+', open(file).read().lower()) 

print(Counter(words).most_common(N)) 
