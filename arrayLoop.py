# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 19:51:40 2018

@author: Ja4rsPC
"""
#print the length of an array.....
print(len('abcdefgh'));

#printing a character of a particular index
print('abc'[2])

#Slicing.......(SubArray)
s = "Jafar Sadik Mohammed"

print(s[6:11])

#Iteration...

ans = 0
x = 3
iteration = x
while (iteration != 0):
    ans = ans + x
    iteration -=1
print(str(x) + ' * ' + str(x) + ' = ' + str(ans) ) 

print(x , ' * ' , x , ' = ' , ans ) 
#the same method that has been used in line 26 wouldn't
#wouldn't work for concatenating the integers with string,
#hence we use commas(,) for concatenatng integer-string    

#find a positive integer that is divisible by both 11 and 12

xx_in = 1

while True:
     if xx_in % 11 == 0 and xx_in % 12 == 0:
         break
     xx_in +=1
print(str(xx_in),' is divisible by both 11 and 12')
         
     
#Using for loop........
#i =0
x_loop = 4
for i in range(0,x_loop):
   print(i)    
   
#for j in range(x_loop,0):
    #print(j)

print("\n")
for j in range(x_loop):
   for i in range(x_loop):
       print(i)
       x_loop=2  #naissssssss.. :'3
       
       
#Finding the cube root of perfect cube

x_cube_root = int(input('Enter an integer: '))
ans_cube = 0
while ans_cube**3 < abs(x_cube_root):
     ans_cube = ans_cube+1
if ans_cube**3 != abs(x_cube_root):
     print(x_cube_root, ' is not a perfect cube')
else:
  if x_cube_root < 0:
     ans_cube = -ans_cube
  print('Cube root of' , x_cube_root, ' is ', ans_cube)
  

#Finding the cube root of perfect cube using for loop

x_cubeRoot_for = int(input('Enter an integer: '))  

for ans_cubeRoot_for in range(0, abs(x_cubeRoot_for)):
    if ans_cubeRoot_for**3 >= abs(x_cubeRoot_for):
        break
if ans_cubeRoot_for**3 != abs(x_cubeRoot_for):
    print(x_cubeRoot_for, 'is not a perfect cube')
else:
    if x < 0:
        ans_cubeRoot_for = - ans_cubeRoot_for
    print('cube root of', x_cubeRoot_for , ' is ', ans_cubeRoot_for)
    
#Approximate Solution and Bisection Search
new_x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans_new = 0.0
while abs(ans_new**2 -new_x) >= epsilon and ans_new <= new_x:
    ans_new += step
    numGuesses +=1
print('numGuesses = ', numGuesses)
if abs(ans_new**2 -new_x) >= epsilon:
    print('failed on square root of ' , new_x)
else:
    print(ans_new, 'is close to square root of ', new_x)    
       
