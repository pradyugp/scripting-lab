#!/usr/bin/python
print("********* Demo: Python does not need data type declaration")
age = 20         # An integer assignment
height   = 6.15       # A floating point
name    = "Munna Bhai"       # A string

#print() is used in Python3 onwards
print("Age is", age)
print("Height is", height)
print("Name is", name)
#To run below line use python2 print age at command prompt
#print age

print("********* Demo: Multiple assignment in one line is possible in python. The data given could be of different types")
age, height, name = 51, 5.91, "Mogembo"

print("Age is", age)
print("Height is", height)
print("Name is", name)

print("********* Demo: Polymorphic Variables - Variables are not bound to a data type once assigned")  
age, height, name = "Gabbar", 5.54, 43

print("Age is", name)
print("Height is", height)
print("Name is", age)
