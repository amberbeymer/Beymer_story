"""
Write a program that will take a number (Integers only) and return a statement that
will let the user know if it is even or odd
"""

x = int(input("Please enter a number (integer please): "))

if (x%2 == 0 ):
    print ("even")

if (x%2 == 1 ):
    print ("odd")