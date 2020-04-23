# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 17:47:40 2020
# Model:
# Make a y variable.
# Make a x variable.
# Change y and x based on random numbers.
# Make a second set of y and xs, and make these change randomly as well.
# Work out the distance between the two sets of y and xs.
@author: bkeight
"""
#modules
import random

#variables
y0 = 50
x0 = 50
y1 = 50
x1 = 50
#-1.random_number = random.random()

# Random walk one step.

#print (y0,x0)
#print (random_number)

#-1.if random_number < 0.5:
if random.random() < 0.5:
    y0 += 1
    x0 += 1
else:
    y0 -= 1
    x0 -= 1
    
if random.random() < 0.5:
    y0 += 1
    x0 += 1
else:
    y0 -= 1
    x0 -= 1

if random.random() < 0.5:
    y1 += 1
    x1 += 1
else:
    y1 -= 1
    x1 -= 1
    
if random.random() < 0.5:
    y1 += 1
    x1 += 1
else:
    y1 -= 1
    x1 -= 1

#print (y0,x0,y1,x1)

#y_diff = (y0 - y1)
#y_diffsq = y_diff * y_diff
#x_diff = (x0 - x1)
#x_diffsq = x_diff * x_diff
#sum = y_diffsq + x_diffsq
#answer = sum**0.5

answer = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5 #raising to 0.5 is the same as the square root
print(answer)

