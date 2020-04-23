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

import random
import operator
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import os
import pathlib
import csv

# Create Variables and blank Lists

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
environment = []
agents = []
fig = matplotlib.pyplot.figure(figsize=(7, 7))
carry_on = True

# Read in data file into Lists

f = open('./in.txt', newline='')    # Open file
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)    # Read file in with CSV library
for row in reader:    # A list of rows
    rowlist = []    # Create blank list
    for value in row:    # A list of value
        rowlist.append(value)   # Append each value read to new list
    environment.append(rowlist)     # Append list to new list
f.close()    # Don't close until you are done with the reader;
# data is read on request.

def update(frame_number):   # Module for creating animation
    
    fig.clear()
#    global carry_on
    
# Make the agents.

    for i in range(num_of_agents):  # Repeat for number of agents
        a = agentframework.Agent(agents, environment)    # Pass arguments to module and return result into a
        agents.append(a)    # Apend a to end of List

# Move the agents.
    
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
       
#def gen_function(b = [0]):
#    a = 0
#    global carry_on #Not actually needed as we're not assigning, but clearer
#    while (a < 10) & (carry_on) :
#        yield a			# Returns control and waits next call.
#        a = a + 1
        
#Plot points

#   maxy = int(max(environment[1]))            # Get maximum value of Y
#   maxx = int(max(environment[0]))            # Get maximum value of x
    matplotlib.pyplot.xlim(0, int(max(environment[1]))) # Set the extent of the Y axis
    matplotlib.pyplot.ylim(0, int(max(environment[0]))) # Set the extent of the X axis
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

animation = matplotlib.animation.FuncAnimation(fig, update, interval=1,repeat=False, frames=num_of_iterations)  # Create animation call
matplotlib.pyplot.show()    # Display graphics

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = agents_row_a.distance_between(agents_row_b)  #
#        print(distance)