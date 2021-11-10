#Demo: Adding functions to class
#Concept: Python "expects" an instance of an object to be present BEFORE a function is called
#Therefore if "s1.insert()"" is called with void brakcets - the code wont compile - if Student Constuctor is undefined
class Person:

  #def __init__(self,name,age):
    #self.name = name;
    #self.age = age;

  def insert(self):
       p3 = self #Creates an instance / object of Person "p3"
       print("\n Printing the contents of local object p3 created with object attributes passed to it - Forrest Gump")
       p3.display(p3)
       print("\n Printing the contents of p1 having object attributes of p2 passed to it - Forrest Gump")
       self.display(p2)

       self.name = input(" Enter the name of Person ") # "input" is used in Python3 onwards
       self.age = input(" Enter the age of Person ") # "raw_input" is used in Python2
       print("\n Printing the contents of object attributes - entered by user")
       self.display(self)
       print("\n Printing the contents of p2 object attributes - changed!!! - entered by user")
       self.display(p2)

  def display(self):
        print("\nName of Person  is", self.name)
        print("\nAge of Person is", self.age)

#s1 = Student("Suppandi", 16) #Constructor commented in this code

p1 = Person
p2 = Person

p2.name = "Forrest Gump!"
p2.age = 38

#si.insert() # This code wont compile if constructor of Person is not defined, that is "__init__" is commented
#p1.insert(p1) #"self" is a placeholder name. The object passed need not be itself as in this case
print("\n Printing the contents of p2 object attributes - changed in insert function!!")
p1.display(p1)
# p3.display(p3) #This wont work, because p3 is defined locally inside insert function
