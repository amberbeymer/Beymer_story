"""
Write a program that will ask the user to
enter their name and respond with a greeting using this name.
"""
print("Please enter your name: ")

x = input()

if (x == "Amber" or x =="amber"):
    print("Hello, Amber!")
    
else:
    print("You are not \'Amber\', but hello anyways!")
    
    
a = int(input('Please enter side a: '))
b = int(input('Please enter side b: '))
c = int(input('Please enter side c: '))

if (a**2 + b**2 == c**2):
    print("This is a right triangle")
    
else:
    print("This is NOT a right triangle")