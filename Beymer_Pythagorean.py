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
    
#Compute the length of the hypotenuse and then return the result in a print statement.
a = float(input("Please enter the length of side a: "))
b = float(input("Please enter the length of side b: "))

c_squared = a**2 + b**2

c = c_squared**0.5

print("The length of hypotenuse is", c)