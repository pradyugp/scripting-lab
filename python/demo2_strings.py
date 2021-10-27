#!/usr/bin/python

print("Python has five datatypes : Number, String, List, Tuple and dictionary")

myStr = 'Hungry Kya'

print(myStr)            # prints complete string
print(myStr[0])         # prints first letter of the string
print(myStr[2:5])       # prints characters from 3rd to 6th letter
print(myStr[2:])        # prints characters from 3rd letter
print(myStr*2)          # prints string two times
print(myStr + "Abhi nahi")  # appends the string

print("Len is:", len(myStr))
print("Replacing ", myStr.replace("Kya", "Abhi"))
print("Splitting ", myStr.split(" "))

print("Number can be integer, float, complex")
a = 3.3
b = 4
c = 4+8j

print(type(a))
print(type(b))
print(type(c))


