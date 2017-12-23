# Exercise 7: Rewrite the grade program from the previous chapter using a
# function called computegrade that takes a score as its parameter and returns a
# grade as a string.
#
# Score   Grade
# > 0.9     A
# > 0.8     B
# > 0.7     C
# > 0.6     D
# <= 0.6    F
#
# Program Execution:
#
# Enter score: 0.95
# A
#
# Enter score: perfect
# Bad score
#
# Enter score: 10.0
# Bad score
#
# Enter score: 0.75
# C
#
# Enter score: 0.5
# F
#
# Run the program repeatedly to test the various different values for input.

def computegrade(score):
    if score < 0.0 or score > 1.0:
        return None
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    else:
        return "F"

raw_score = input("Enter Score: ")
try:
    score = float(raw_score)
except:
    print("Bad score")
    quit()
    
grade = computegrade(score)
if grade is None:
    print("Bad score")
else:
    print(grade)
