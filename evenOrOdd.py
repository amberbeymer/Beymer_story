"""
Write a program that will take a number (Integers only) and return a statement that
will let the user know if it is even or odd
"""

x = float(input("Please enter a number (integer please): "))

if (x%2 == 0 ):
    print ("This is an even number!")

elif (x%2 == 1 ):
    print ("This is an odd number!")
    
else:
    print ("This is not an integer, dude")