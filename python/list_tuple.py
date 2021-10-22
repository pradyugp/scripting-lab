#!/usr/bin/python

# All items belonging to a list can be of a different datatype. Items are enclosed within [ ]
# List elements and ssize can be changed

print("Demo list manipulation: ")
list1 = ['tintin', 22, 5.43, "Belgium", 'Day Detective']
list2 = ['haddock', 45, 6.1, 'Netherlands', 'side guy']

print(list1)
print(list1[0])             # prints first element
print(list1[1:3])
print(list1[2:])            # prints 3rd element onwards
print(list1*2)
print(list1 + list2)

# TUPLE also contains different data types they are enclosed in {  }
# TUPLES are immutable that means values cannot be changed

print('Tuple manipulation:  ')

myTuple = ("TinTin", 22, 5.43, 'Belgium', 'Boy detective')

print(myTuple)
print(myTuple[0])             # prints first element
print(myTuple[1:3])
print(myTuple[2:])            # prints 3rd element onwards
print(myTuple*2)
print(myTuple + myTuple)

yourTuple = ('haddock', 35, 6.10, 'Luxembourg', 'Sidechar')

print(myTuple + yourTuple)



