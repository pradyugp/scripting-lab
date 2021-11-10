#Demo: Classes in Python
#Concept: Use of del function to delete attributes of an object and an object itself

class Person:
  def __init__(self,name,age): #This is the constructor of the class Person
    self.name = name;
    self.age = age;


p1 = Person("Suppandi", 14)


print("\nName of Person  is", p1.name)
print("\nAge of Person  is", p1.age)


print("\n*** Printing after deleting age attribute for p1****")
del p1.age #Deleting the age attribute for p1 object
print("\nName of Person #1 is", p1.name)
#print("\nAge of Person #1 is", p1.age) #This line will give an error!!!
#Error is: AttributeError: 'Person' object has no attribute 'age'

print("\n*** Printing after deleting p1****")
del p1
print("\nName of Person #1 is", p1.name) #This line will give an error!!!
#Error is: NameError: name 'p1' is not defined
