# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume the user types numbers properly.

hrs = input("Enter Hours:")
h = float(hrs)
payment_rate = 10.5

if h > 40:
    extra_h = h - 40 
    normal_h = 40
    payment_extra = extra_h * (payment_rate*1.5)
    payment_normal = payment_rate * normal_h
    payment = payment_extra +payment_normal
    print(payment)
else:
    payment = h * payment_rate
    print(payment)    



