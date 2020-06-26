# Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
hrs = input("Enter Hours:")
hrs = float(hrs)
rate = input("Enter the Rate:")
rate = float(rate)
pay = hrs * rate
print("Pay:", hrs * rate)
