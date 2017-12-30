# Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
# the document from a URL, (2) displaying up to 3000 characters, and (3)
# counting the overall number of characters in the document. Don't worry about
# the headers for this exercise, simply show the first 3000 characters of the
# document contents.

import urllib.request

url = input("Please enter a URL:")
try:
    fhand = urllib.request.urlopen(url)
except Exception as e:
    print(e)
    exit()

count = 0
for line in fhand:
    text = line.decode().strip()
    count += len(text)
    if count > 3000:
        continue
    print(text)

print("total number of characters:", count)
