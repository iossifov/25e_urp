import requests
text = requests.get("https://www.gutenberg.org/cache/epub/1524/pg1524.txt").text
nas = 0
for s in text:
    if s == 'a':
        nas += 1
print(f"'a' is seen {nas} times.")
from collections import Counter
wcd = Counter(text.split())
max_wc = max(wcd.values())
most_common_words = [w for w, wc in wcd.items() if wc == max_wc]
print(f"The most common word is {most_common_words} and it is seen {max_wc} times.")
