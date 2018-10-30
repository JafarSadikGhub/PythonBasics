# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 22:36:35 2018

@author: Ja4rsPC
"""
#A recursive function to finding a fibonacci sequence

n = int(input('Input an integer: '))

    
    
def fib(n_n):
    if n_n<2:
        return n_n
    else:
        return (fib(n_n-1)+fib(n_n-2))

for i in range(1,n+1):
    print(fib(i))
    
    
    
print('The number is:' ,fib(n))    