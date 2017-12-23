# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and
# rate).
#
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def computepay(hours, rate):
    if hours > 40:
        return 40 * rate + (hours - 40) * rate * 1.5
    else:
        return hours * rate

raw_hours = input("Enter Hours:")
hours = float(raw_hours)
raw_rate = input("Enter Rate:")
rate = float(raw_rate)

print("Pay:", computepay(hours, rate))
