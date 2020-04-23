# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 16:46:40 2020

@author: bkeight
"""

#names = ("Dale", "Albert", "Gordon", "Tamara", "Philip", "Chester", "Windom") 
#for i in range(len(names)):
#    print(i, names[i])


#looping
'''
names = ("Dale", "Albert", "Gordon", "Tamara", "Philip", "Chester", "Windom") 
for i in range(2,len(names),2):
    print(names[i])
    
for name in names[2::2]:
    print(name)
    
for name in names[:]:	# Note full slice
    names.remove(name)
print(names)
'''
#2d looping
'''
data = [
[0,1,2],
[3,4,5],
[6,7,8]
]
'''

#for row in data:
#    for item in row:
#        print (item)
''' 
for i in range(len(data)):
    for j in range(len(data[i])):
        print (data[i][j], end=",")
    print ("")

#For a know dataset
data = [
[0,1],
[2,3],
[4,5]
]

for a,b in data:
    print (str(a) + " " + str(b))
'''

#For 2 datasets (zipping)
'''
a = [1,2,3,4,5]
b = [10,20,30,40,50]
z = zip(a,b)
d = {}
for t in z:
    d[t[0]] = t[1]
print(d)
'''

#
'''
a = list(range(3))
it = iter(a)
for i in range(5):
    print(next(it, "missing"))

a = list(range(3))
ri = reversed(a)
for i in ri:
    print(i)
'''
'''
a = ["f","b","d","c","a"]
b = sorted(a)

#Boundary wall effect
import random
agents = [] #creates empty list agents
i = 1
# Move agent.
if random.random() < 0.5:
    agents[i][0] += 1
else:
    agents[i][0] -= 1
# Check if off edge and adjust.
if agents[i][0] < 0:
    agents[i][0] = 0
if agents[i][1] < 0:
    agents[i][0] = 0
if agents[i][0] > 99:
    agents[i][0] = 99
if agents[i][1] > 99:
    agents[i][0] = 99

#Torus
'''
#Functions
#Help - https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference
#     - https://www.python.org/dev/peps/pep-0448/

'''
#Packing using Tuples in Functions
def sum (num1, num2, *others):
    sum = num1
    sum += num2
    for num in others:
        sum += num
    return sum
answer = sum(1,2,3,4,5,6,7)
print(answer)
'''

'''
#Unpacking using Tuples in Functions
def sum (num1, num2, num3, num4):
    return num1 + num2 + num3 + num4

a = [1,2,3,4]
answer = sum(*a)
print(answer)
'''
'''
#Packing & Unpacking at same time
def sum(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

a = [1,2,3]
answer = sum(*a)
print(answer)
'''
'''
#Packing using Dictionary in Functions
def print_details (a, **details):
    first = details["first"]
    surname = details["surname"]
    print (first + " " + surname + " has " + a + " pounds")

print_details("5", first="George", surname="Formby")
'''
'''
#Upacking with Dicts
def print_details(a, first, surname):
    print (first + " " + surname + " has " + a + " pounds")

d = {"first":"George","surname":"Formby"}
print_details("5",**d)
'''

'''
#####
# This is an example of Object programing and using self

# Main program 

import agentframework
agent_1 = agentframework.Agent()
agent_1.y = 100
agent_1.x = 50
print(agent_1.y)	


# agentframework.py

class Agent():
    def __init__ (self):
        self.y = None
        self.x = None
'''

'''
# Main program 
import agentframework
agent_1 = agentframework.Agent()
agent_1.randomize()
print(agent_1.y, agent_1.x)	

# agentframework.py
import random
class Agent():
    def __init__(self):
        self.y = None
        self.x = None
    def randomize(self):
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
'''
'''
class EvenInt(int):

    def __init__(self, i):
        #print(self)
        #print(i)
        self.value = i
        #print(self.value)

    def __add__(self, other):
        print(self)
        print(other)
        if (self.value + other) % 2 == 1:
            return (self.value + other + 1)
        else:
            return (self.value + other)

a = EvenInt(3)
b = a + 2
print(b)

class EvenInt(int):


    def __init__(self, i):
        self.value = i
        
    def __add__(self, other):
        if (self.value + other) % 2 == 1:
            return (self.value + other + 1)
        else:
            return (self.value + other)
     
    def __radd__(self, other):
        return self.__add__(other)
     
a = EvenInt(3)
b = a + 2
c = 2 + a
print(b)
print(c)

#parsing
f = open("in.txt")
data = []
for line in f:
    parsed_line = str.split(line,",")
    data_line = []
    for word in parsed_line:
        data_line.append(float(word))
    data.append(data_line)
print(data)
f.close()

#Writing multiple files
import fileinput
a = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]
b = fileinput.input(a, inplace=1, backup='.bak')
for line in b:
    print("new text")
b.close()

inplace = 1	# Redirects the stout (i.e. print) to the file.
backup ='.bak'	# Backs up each file to file1.txt.bak etc. before writing.


import os
os.getcwd() # Current working directory.
os.chdir('/temp/') # Change cwd. 
os.listdir(path='.')	# List of everything in the present directory.
os.system('mkdir test') # Run the command mkdir in the system shell
'''
import os
import pathlib
a = os.path.join(pathlib.Path.cwd().anchor, 'Program Files', 'Notepad++')
p = pathlib.Path(a) 
print (str(p))  #c:\Program Files\Notepad++
print (repr(p)) #WindowsPath('C:/Program Files/Notepad++')
p.name     # final path component.
p.stem	    # final path component without suffix.
p.suffix     # suffix.
p.as_posix()     # string representation with forward slashes (/):
p.resolve()     # resolves symbolic links and ".."
p.as_uri()	    # path as a file URI: file://a/b/c.txt
p.parts     # a tuple of path components.
p.drive     # Windows drive from path. 
p.root     # root of directory structure.
pathlib.Path.cwd()	    # current working directory.
pathlib.Path.home()    # User home directory

#Functions for checking the properties of actual files: 
p.is_absolute()	    # Checks whether the path is not relative.
p.exists()     # Does a file or directory exist.
os.path.abspath(path)	    # Absolute version of a relative path.
os.path.commonpath(paths)     # Longest common sub-path. 
p.stat()     # Info about path (.st_size; .st_mtime) 
https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat
p.is_dir()     # True if directory.
p.is_file()	    # True if file.
p.read()	    # A variety of methods for reading files as an entire object, rather than parsing it.

#Listing subdirectories:
import pathlib

p = pathlib.Path('.')
for x in p.iterdir():
    if x.is_dir():
        print(x)

# Functions for checking the properties of actual files: 
p.rename(target)	#Rename top file or directory to target.
p.with_name(name)	#Returns new path with changed filename. 
p.with_suffix(suffix)	#Returns new path with the file extension changed.
p.rmdir()	Remove directory; #must be empty.
p.touch(mode=0o666, exist_ok=True) "Touch" file; i.e. make empty file.
p.mkdir(mode=0o666, parents=False, exist_ok=False) #Make directory.

a = list(p.glob('**/*.txt'))
a = sorted(p('.').glob('*.csv'))

import numpy
data = numpy.int_([
[1,2,3,4,5],
[10,20,30,40,50],
[100,200,300,400,500]
])

print(data[0,0])	# 1
print(data[1:3,1:3])	# [[20 30][200 300]]
print(data[1:3,1:3] - 10) # [[10 20],[190 290]]
print(numpy.transpose(data[1:3,1:3]))	# [[20 200],[30 300]]
