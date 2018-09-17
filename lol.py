"""
Write a program that will ask the user for a number (integers only) and return a
a statement that the number is EVEN or ODD
"""

x = float(input("Please enter a number: "))

if (x%2 == 0):
    print("The number " + str(x) + " is even!")
    
else:
   print("The number " + str(x) + " is odd!")
