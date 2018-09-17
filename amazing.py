"""
This program demonstrates IMPORT statements and LOOPS.
"""

#import statements go FIRST! (TOP OF YOUR CODE)
import time
 
# for variableName in range(start, stop, step):
# OR
# for variableName in range(stop): *This will start 0 and step by 1
 
for i in range (1,11):
    print ('Hello' + str(i))
    
# Count to 100 by 5's

for i in range (5, 103, 5):
    print (str(i))
    
# Count down from (START AT 20) by 2's and stop at -4

for i in range(20, -5, -2):
    print (str(i))
    
#Print 10 random integers between -100 amd 1000
import random
