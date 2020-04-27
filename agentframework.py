# -*- coding: utf-8 -*-
"""
# Module Created on Tue Apr  7 20:29:34 2020
#
# agentframework:
#
#
# @author: bkeight
"""

# Libraries required

import random

class Agent():
        
    def __init__(self, agents, environment, y, x):        # Constructor with 2 additional arguments
        self.agents = agents                        # Pass agents argument
        self.y = y               # set y to a random No. between 0 & Max Y value
        self.x = x               # set y to a random No. between 0 & Max X Value
        self.environment = environment              # Pass environment argument
        self.store = 0                              # We'll come to this in a second.
    
    def move(self):
        if random.random() < 0.5:                   # random = value between 0 and <1
            self.y = (self.y + 1) % 100             # agents[i][0] += 1 # y
            self.x = (self.x + 1) % 100             # agents[i][1] += 1 # x
        else:
            self.y = (self.y - 1) % 100             # agents[i][0] -= 1 # y
            self.x = (self.x - 1) % 100             # agents[i][1] -= 1 # x

    def eat(self): # 
        if self.environment[self.y][self.x] > 10:   #
            self.environment[self.y][self.x] -= 10  #
            self.store += 10                        #

    def distance_between(self, agent):
        return (((self.x - agent.x)**2) 
                + ((self.y - agent.y)**2))**0.5
    
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent) 
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave                   #
#                print("sharing " + str(dist) + " " + str(ave))         # Test
