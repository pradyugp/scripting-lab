#Write a Python Program to read the contents of a file
# a) Print line by line
# b) Seperate each word of a line, store it in a list and print the same 
escape = open('HakunaMatata')

worddic = { }
for line in escape:
 print (line)
 myline = line.split()
 print (myline)
