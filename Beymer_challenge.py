
"""
Write a program that will ask the user to enter in three legs of a triangle
and then test to see if the triangle is:
"""
#Not a triangle (a + b < c)
a = float(input ("Please enter a positive value, a: "))
b = float(input ("Please enter a positive value, b: "))
c = float(input ("Please enter a positive value, c: "))

s = (a + b - c) * (a + c - b) * (c + b - a)

#"The smallest representable positive number such that 1.0 + eps != 1.0.
#Type of eps is an appropriate floating point type."
eps = 0.0000001

if abs(s) > eps:
    print ("This is a triangle.")
else:
    print ("This is not a triangle.")
    
#A right triangle
a = int(input('Please enter side a: '))
b = int(input('Please enter side b: '))
c = int(input('Please enter side c: '))

if (a**2 + b**2 == c**2):
    print("This is a right triangle")
    
else:
    print("This is NOT a right triangle")
    
#An Obtuse triangle (a**2 + b**2 < c**2)
a = float (input ("Please enter a positive value, a: "))
b = float (input ("Please enter a positive value, b: "))
c = float (input ("Please enter a positive value, c: "))

s = (a**2 + b**2 - c**2) * (a**2 + c**2 - b**2) * (c**2 + b**2 - a**2)

eps = 0.0000001

if abs(s) > eps:
    print ("This is an obtuse triangle.")
else:
    print ("This is not an obtuse triangle.")

#An acute triangle (a**2 + b**2 > c**2)
a = float(input ("Please enter a positive value, a: "))
b = float(input ("Please enter a positive value, b: "))
c = float(input ("Please enter a positive value, c: "))

s = (a**2 + b**2 - c**2) * (a**2 + c**2 - b**2) * (c**2 + b**2 - a**2)

eps = 0.0000001

if abs(s) < eps:
    print ("This is an acute triangle.")
else:
    print ("This is not an acute triangle.")



