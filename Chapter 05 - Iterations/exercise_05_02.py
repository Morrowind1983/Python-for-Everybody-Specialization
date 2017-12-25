# Exercise 1: Write a program which repeatedly reads numbers until the user
# enters "done". Once "done" is entered, print out the total, count, and average
# of the numbers. If the user enters anything other than a number, detect their
# mistake using try and except and print an error message and skip to the next
# number.
#
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5.333333333333333
# 
# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum of the numbers instead
# of the average.

max_num = None
min_num = None

while True:
    raw_string = input("Enter a number: ")
    if raw_string == "done":
        break
    try:
        num = int(raw_string)
    except:
        print("Invalid input")
        continue
    if max_num is None or num > max_num:
        max_num = num
    if min_num is None or num < min_num:
        min_num = num

print("Maximum is", max_num)
print("Minimum is", min_num)
