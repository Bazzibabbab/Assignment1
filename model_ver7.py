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
import matplotlib
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
#import os
#import pathlib
import csv
import tkinter

# Create Variables and blank Lists

num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
environment = []
agents = []
fig = matplotlib.pyplot.figure(figsize=(7, 7))
carry_on = True
matplotlib.use('TkAgg')

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
    
# Make the agents.

    for i in range(num_of_agents):  # Repeat for number of agents
        a = agentframework.Agent(agents, environment)    # Pass arguments to module and return result into a
        agents.append(a)    # Apend a to end of List

# Move the agents.
    
    for j in range(num_of_iterations):  # For each entry do...
        for i in range(num_of_agents):  # For each entry do...
            agents[i].move()    # Move the agent
            agents[i].eat()     # Eat the agent
            agents[i].share_with_neighbours(neighbourhood)
       
       
#Plot points

    matplotlib.pyplot.xlim(0, int(max(environment[1]))) # Set the extent of the Y axis
    matplotlib.pyplot.ylim(0, int(max(environment[0]))) # Set the extent of the X axis
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1,repeat=False, frames=num_of_iterations)  # Create animation call
    canvas.show()

root = tkinter.Tk() # Create the root window
root.wm_title("Model")  # Title of main window set to "Model"
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root) # Set out the Canvas to build the GUI on
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)    # Displays the canvas on the screen
menu_bar = tkinter.Menu(root)   # Create a pulldown menu class
root.config(menu=menu_bar)  # Use the option menu_bar to create the new menu
model_menu = tkinter.Menu(menu_bar) # Creates the menu
menu_bar.add_cascade(label="Model", menu=model_menu) # Creates the cascade menu
model_menu.add_command(label="Run model", command=run) # Creates the option "Run Model" which will activate the run function

for agents_row_a in agents:
    for agents_row_b in agents:
        distance = agents_row_a.distance_between(agents_row_b)  #
#        print(distance)
        
tkinter.mainloop() # Wait for user to interact with widget
