#!/usr/bin/python
print("Python has five data types : Number, String, List, Tuple, Dictionary")

print("\n *****Demo : String Manipulations")

mystr = 'Hungry Kya!'

print(mystr)          # Prints complete string
print(mystr[0])       # Prints first character of the string
print(mystr[2:5])     # Prints characters starting from 3rd to 5th
print(mystr[2:])      # Prints string starting from 3rd character
print(mystr * 2)      # Prints string two times
print(mystr + " Abhi Nahin") # Prints concatenated string
print("Length is", len(mystr))
print("Replacing ", mystr.replace("Kya","?"))
print("Splitting", mystr.split(" "))

print("\n *****Demo : Number - Python can handle integer, float and complex")
x = 33    # int
y1 = 9.87  # float
y2  = -87.7e100
z = 4j   # complex
print(type(x))
print(type(y1))
print(type(y2))
print(type(z))
