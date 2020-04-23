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



agents = [] #creates empty list agents
num_of_agents = 10 #max number of agents
num_of_iterations = 100


for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)]) # creates a random value for y & x
    
for j in range(num_of_iterations):
    for i in range(num_of_agents): # repeat loop num_of_agents times
        if random.random() < 0.5: # random = value between 0 and <1
            agents[i][0] = (agents[i][0] + 1) % 100
#            agents[i][0] += 1 # y
            agents[i][1] = (agents[i][1] + 1) % 100
#            agents[i][1] += 1 # x
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
#            agents[i][0] -= 1 # y
            agents[i][1] = (agents[i][1] - 1) % 100
#            agents[i][1] -= 1 # x

answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5 #raising to 0.5 is the same as the square root

matplotlib.pyplot.ylim(0, 99) # Get or set the y-limits of the current axes
matplotlib.pyplot.xlim(0, 99) # Get or set the x limits of the current axes
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0]) # A scatter plot of agents[num_of_agents]
east = max(agents, key=operator.itemgetter(1))
matplotlib.pyplot.scatter(east[1],east[0], color='red')
matplotlib.pyplot.show() # Display all figures
