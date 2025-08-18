from collections import Counter

with open("sample.txt", "r") as f:
    text = f.read()
    
words = text.split()

word_count = Counter(words)

with open("results.txt", "w") as f:
    for word, count in word_count.items():
        f.write(f"{word}: {count}\n")
