# -*- coding: utf-8 -*-
"""
# Created on Fri Mar 13 17:47:40 2020
#
# model:
#
# Create a List to hold the new coordinates
# Create random number for coordinates.
# Add the new y,x as a List within a List.
# Append further coordiantes to the List of Lists.
# Work out the distance between the two sets of y and xs.
#
@author: bkeight
"""
# Libraries required

#import random
#import operator
import matplotlib.pyplot
import agentframework
#import os
#import pathlib
import csv

#def distance_between(agents_row_a, agents_row_b):
#    return (((agents_row_a.x - agents_row_b.x)**2) + ((agents_row_a.y - agents_row_b.y)**2))**0.5

# Create Variables and blank List
num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
environment = []
agents = []

# Read in data file into Lists

f = open('in.txt', newline='')                          # Open file
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)    # Read file in with CSV library
for row in reader:                                      # A list of rows
    rowlist = []                                        # Create blank list
    for value in row:                                   # A list of value
        rowlist.append(value)                           # Append each value read to new list
    environment.append(rowlist)                         # Append list to new list
f.close()                                               # Don't close until you are done with the reader;
# data is read on request.

# Make the agents.

for i in range(num_of_agents):
    a = agentframework.Agent(agents, environment)       # Pass arguments to module and return result into a
    agents.append(a)                                    # Apend a to end of List
#    agents.append(agentframework.Agent(environment))
#    a = agentframework.Agent(environment)
#    print("x=", a.y, a.x)

# Move the agents.
    
for j in range(num_of_iterations):
    for i in range(num_of_agents):
       agents[i].move()
       agents[i].eat()
       agents[i].share_with_neighbours(neighbourhood)

#Plot points

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()

for agents_row_a in agents:
    for agents_row_b in agents:
#        distance = distance_between(agents_row_a, agents_row_b)
        distance = agents_row_a.distance_between(agents_row_b)  #
