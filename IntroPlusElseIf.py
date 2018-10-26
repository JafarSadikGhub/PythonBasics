# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("How you doing?")

a = 1;
print(a);

c = "hello there!"
print(c)

v1 = "first string"
v2 =  "second string"
temp1 = v1
v1= v2
v2 = temp1

print(v1)
print(v2)

radius = 5
pi = 3.1416
area = pi*(radius**2)

print(round(area))


yourvar = input('Choose a number: ')
print('you entered: ' + yourvar)

name= input('Enter your name: ')
print('Your name is : ' + name);

print(name + ' Your age is ' + yourvar)

#x = input('')
#print(x)

#Reading integer................
x = int(input('Please input the value of x : '))

#num = 3.4

# Try these two variations as well:
# num = 0
# num = -4.5

if x > 0:
    print("Positive number")
elif x == 0:
    print("Zero")
else:
    print("Negative number")
    
    
if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x%3 == 0:
        print('Divisible by 3 and not by 2')
    
st1 = " Ami to bhala na bhala loiyai thaiko "
st2 = 1000* st1
print(st2)            
            
            
            












