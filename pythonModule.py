# Using My Module
import myModule
myModule.greeting("shukla")

import myModule as mx
a=mx.person1["country"]
print(a)

a=mx.person1["age"]
print(a)

#...........................................................................

# there are so many built in module in python
import platform
x=platform.system()
print(x)

import os 
# current working directory
cwd = os.getcwd()
print(cwd)

# change directory
os.chdir('c:/class-python')
cwd=os.getcwd()
print(cwd)

import datetime
x=datetime.datetime.now()
print(x)
# the date contains year, moths, day, hours, min, sec, microsec.
# year
print(x.year)

# day
print(x.strftime("%A"))

# months
print(x.strftime("%B"))

# for more info search for datetie module in W3schools

# math module
x=min(5,10,25)
y=max(5,10,25)
print(x)
print(y)

# absloute value
x=abs(-7.25)
print(x)

import math
x=math.sqrt(64)
print(x)

# round upword to nearest whole number
x=math.ceil(1.4)
print(x)

# round downword to nearest whole number
x=math.floor(1.4)
print(x)

x=math.pi
print(x)