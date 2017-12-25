# Exercise 4: Add code to the above program to figure out who has the most
# messages in the file.
# After all the data has been read and the dictionary has been created, look
# through the dictionary using a maximum loop (see Section [maximumloop]) to
# find who has the most messages and print how many messages the person has.
#
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
#
# Enter a file name: mbox.txt
# zqian@umich.edu 195

fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

counts = dict()
for line in fhand:
    if not line.startswith("From:"):
        continue
    words = line.split()
    if len(words) < 2:
        continue
    email = words[1]
    if '@' not in email:
        continue
    counts[email] = counts.get(email, 0) + 1

max_num = None
max_person = None
for email in counts:
    num = counts[email]
    if max_num is None or num > max_num:
        max_num = num
        max_person = email
print(max_person, max_num)
