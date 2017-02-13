import re
import os
from collections import Counter

words = re.findall(r'\w+', open('hamlet.txt').read().lower())
e = ('the', 'and', 'to', 'of', 'i', 'a', 'you', 'my', \
'in', 'it', 'that', 'is', 'not', 'd', 'his', 'this',\
'with', 'but', 'for', 'your', 's', 'me', 'as', 'be',\
'what', 'him', 'he', 'so')

i = 0
for w in words[::]:
    if w in e:
        del words[i]
    else:
        i += 1

print(Counter(words).most_common(30))