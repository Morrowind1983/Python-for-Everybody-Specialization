# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the
# hourly rate for hours worked above 40 hours.
# 
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

raw_hours = input("Enter Hours:")
hours = float(raw_hours)
raw_rate = input("Enter Rate:")
rate = float(raw_rate)
    
if hours > 40:
    pay = 40 * rate + (hours - 40) * rate * 1.5
else:
    pay = hours * rate
    
print("Pay:", pay)
