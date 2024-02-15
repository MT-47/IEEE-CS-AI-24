from collections import Counter #searched for this line

with open('Sample.txt') as file:
    text = file.read()

word_counts = Counter(text.split())

for word, count in word_counts.items():
    print(f"{word}: {count}")
