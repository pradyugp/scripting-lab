
#Demo: Adding functions to class
#Concept: Class Variable shared by all objects of class. Here "personCount"
#This program gives the number of Person objects created
class Person:
  'Class Variable shared by all objects of class. Here "personCount"'
  personCount = 0
  def __init__(self,name,age):
    self.name = name;
    self.age = age;
    Person.personCount = Person.personCount + 1

  def display(self):
        print("\nName of Person  is", self.name)
        print("\nAge of Person  is", self.age)
        print("The Total number of person objects is %d" %Person.personCount)

print("Person.__doc__:", Person.__doc__)
print("Person.__name__:", Person.__name__)
print("Person.__module__:", Person.__module__)
print("Person.__bases__:", Person.__bases__)
print("Person.__dict__:", Person.__dict__)
