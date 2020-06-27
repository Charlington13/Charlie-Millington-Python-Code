# Write a program to prompt for a score between 0.0 and 1.0. 
# If the user enters a value out of range, print a suitable error message and exit

score = input("Enter Score: ")
sc = float(score)
if sc >= 1.0:
	print ('Enter a value between 0.0 to 1.0')
elif sc < 0.0:
	print ('Enter a value between 0.0 to 1.0')

if sc >= 0.9:
    x = 'A'

elif sc >= 0.8:
    x = 'B'

elif sc >= 0.7:
    x = 'C'
    
elif sc >= 0.6:
    x = 'D'

elif sc < 0.6:
    x = 'F'

else:
    x = 'check the value'
print (x)
    
quit ()
