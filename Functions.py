# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 00:36:25 2018

@author: Ja4rsPC
"""

x = int(input('Please input integer 1:' ))
y = int(input('Please input integer 2: '))
 
def maxVAlue(m,n):
    if m>n or m==n:
        return m
    else:
        return n


print(maxVAlue(x,y), ' Is greatest') 

#Scoping

def f(x):
    y = 1
    x = x + y
    print('x = ', x)
    return x

x = 3
y = 2
z = f(x)
print('z =', z)
print('x =', x)
print('y =', y)


    
    
    
    