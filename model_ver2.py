# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 17:47:40 2020
# Model:
# Create a List to hold the new coordinates
# Create random number for coordinates.
# Add the new y,x as a List within a List.
# Append further coordiantes to the List of Lists.
# Work out the distance between the two sets of y and xs.
@author: bkeight
"""
#modules
import random
import operator
import matplotlib.pyplot # exteranl module

#variables
#y0 = 50
#x0 = 50
#y1 = 50
#x1 = 50
#or assign vaviables

agents = [] #creates empty list agents

#y0 = random.randint(0,99)
#x0 = random.randint(0,99)

#agents.append([y0,x0]) #adds variables as a list [] to the list agent
agents.append([random.randint(0,99),random.randint(0,99)]) # removes the need to create y0 and x0
agents.append([random.randint(0,99),random.randint(0,99)])
#-1.random_number = random.random()

# Random walk one step.

#print (y0,x0)
#print (random_number)

#-1.if random_number < 0.5:
if random.random() < 0.5:
    agents[0][0] += 1
    agents[0][1] += 1
else:
    agents[0][0] -= 1
    agents[0][1] -= 1
    
if random.random() < 0.5:
    agents[0][0] += 1
    agents[0][1] += 1
else:
    agents[0][0] -= 1
    agents[0][1] -= 1

if random.random() < 0.5:
    agents[1][0] += 1
    agents[1][1] += 1
else:
    agents[1][0] -= 1
    agents[1][1] -= 1
    
if random.random() < 0.5:
    agents[1][0] += 1
    agents[1][1] += 1
else:
    agents[1][0] -= 1
    agents[1][1] -= 1

#print (y0,x0,y1,x1)

#y_diff = (y0 - y1)
#y_diffsq = y_diff * y_diff
#x_diff = (x0 - x1)
#x_diffsq = x_diff * x_diff
#sum = y_diffsq + x_diffsq
#answer = sum**0.5

print (agents) # print agents list
print(max(agents)) # Retruns the pair of coordiantes with highest value of y to the screen
print(max(agents, key=operator.itemgetter(1))) # Retruns the pair of coordiantes with highest value of x to the screen

answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5 #raising to 0.5 is the same as the square root
print(answer)

matplotlib.pyplot.ylim(0, 99) # Get or set the y-limits of the current axes
matplotlib.pyplot.xlim(0, 99) # Get or set the x limits of the current axes
matplotlib.pyplot.scatter(agents[0][1],agents[0][0]) # A scatter plot of y0 vs x0
matplotlib.pyplot.scatter(agents[1][1],agents[1][0]) # A scatter plot of y1 vs x1
east = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(east[1],east[0], color='red')
matplotlib.pyplot.show() # Display all figures
