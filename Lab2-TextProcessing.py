# Pack
# from nltk.tokenize import regexp_tokenize
import nltk
from nltk import regexp_tokenize

nltk.download('punkt')
import pickle
from collections import Counter

# Read text file

with open('data/Lab2Text.txt', encoding="utf8") as txt:
    text = txt.read().lower()


# Create function that counts each word and use it to define a dictionary
def wordCount(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


wordDict = wordCount(text)
print(wordDict)

# Create sorted dict then use index for frequency check
sorted_Dict = sorted(wordDict.items(), key=lambda i: -i[1])

most_freq = sorted_Dict[:1]
least_freq = sorted_Dict[::-1]

# Word Count
words = text.split()
len(words)

# Unique Word Count
len(least_freq)

# Tokenisation
# Using a regex based tokenizer in NLTK, other tokenizers required more support.

tokens = nltk.word_tokenize(text, pattern='\s+', gaps=True)

print(tokens)

# Word Counting with NLTK - Most and Least
freq_nltk = nltk.FreqDist(tokens)
print(freq_nltk.most_common(5))
print(freq_nltk.most_common()[-5:])

# Count of words used
len(freq_nltk)

# Count of unique words used

unique = list(filter(lambda x: x[1] == 1, freq_nltk.items()))
print(unique)


