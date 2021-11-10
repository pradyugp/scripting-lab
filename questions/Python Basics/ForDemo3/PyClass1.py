#Demo: Classes in Python
#Notice the use of "self". It is the first argument passed to any function.

class Person:
  def __init__(self,name,age): #This is the constructor of the class Person
    self.name = name;
    self.age = age;

#Two objects s1 and s2 are created. The __init__ constructor is autonmatically called
p1 = Person("Suppandi", 14)
p2 = Person("Ramu", 12)

print("\nName of Person #1 is", p1.name)
print("\nAge of Person #1 is", p1.age)

print("\nName of Person #2 is", p2.name)
print("\nAge of Person #2 is", p2.age)

p2.age = 10 #Attributes of the object can be modified like this. By default public

print("\nModified Age of Person #2 is", p2.age)
