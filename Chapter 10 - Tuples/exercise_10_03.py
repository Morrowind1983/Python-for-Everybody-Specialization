# Exercise 3: Write a program that reads a file and prints the letters in
# decreasing order of frequency. Your program should convert all the input to
# lower case and only count the letters a-z. Your program should not count
# spaces, digits, punctuation, or anything other than the letters a-z. Find text
# samples from several different languages and see how letter frequency varies
# between languages. Compare your results with the tables at
# wikipedia.org/wiki/Letter_frequencies.

fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

counts = dict()
for line in fhand:
    line = line.lower()
    for word in line:
        if word < 'a' or word > 'z':
            continue
        counts[word] = counts.get(word, 0) + 1

sorted_counts = sorted(counts.items(), key=lambda x:x[1], reverse=True)
for key, value in sorted_counts:
    print(key, value)
