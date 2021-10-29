# Demo: CLasses in python
# Concept: Use of del function to delete attributes and an object itself

class Person:
    def __init__(self,name,age): # This is the constructor of the class person
        self.name = name
        self.age = age

# Two objects s1 and s2 are created. The__init__ constructor is automatically called 
p1 = Person("Suppandi", 14)
p2 = Person("Shambhu", 23)

print("\nName of Person1 is ", p1.name)
print("\nage of Person2 is", p1.age)

print("\n *** Printing after deleting age attribute for p1 ***")
del p1.age # This deletes the age attribute for p1 obj
print("\nName of the person #1 is ", p1.name)
# print("\nAge of Person 1 is", p1.age) **This line gives an error 

print("\n*** Printing after deleting p1***")
del p1
# print("\nnAME OF pERSON #1 IS ", p1.name)
# The above line also will give an error
