#Demo: Adding functions to class
#Concept: Python classes without constructors are ambiguous
class Person:

  #def __init__(self,name,age):
    #self.name = name;
    #self.age = age;

  def display(self):
        print("\nName of Person  is", self.name)
        print("\nAge of Person  is", self.age)

#s1 = Student("Suppandi", 16) #Constructor commented in this code

p1 = Person
p2 = Person

#Copy & Paster p1.name and p1.age AFTER p2.name and p2.age and see!!
#Python is taking the most recently created object and passing it as parameter to display
#Reason: display(self) expects any object of Person and p2 is a valid object!!
#Therefore it is better to use constructors!

p1.name = "Private Ryan!"
p1.age = 25

p2.name = "Forrest Gump!"
p2.age = 38

print("\n Printing the contents of p1 object attributes - WRONGLY!!")
p1.display(p1) #If  constructor is defined then "pi" need not be passed as argument to display 
