#!/usr/bin/env python3
x = int(input('Enter the first number:')) 
y = int(input('Enter the second number:'))
print(x,'X', y , ' =',x * y)
if x * y > 0: 
    print("The result is positive.")
elif x * y < 0: 
    print("The result is negative.")
else: 
    print("This result is both positive and negative.")
