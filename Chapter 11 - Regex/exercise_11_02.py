# Exercise 2: Write a program to look for lines of the form
#
# `New Revision: 39772`
#
# and extract the number from each of the lines using a regular expression and
# the findall() method. Compute the average of the numbers and print out the
# average.
#
# Enter file:mbox.txt
# 38549.7949721
#
# Enter file:mbox-short.txt
# 39756.9259259

import re

fname = input("Enter file:")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

revs = list()
for line in fhand:
    line = line.rstrip()
    lst = re.findall('New Revision: (\d+)', line)
    if len(lst) > 0:
        revs.append(int(lst[0]))
    
print(sum(revs) / len(revs))
