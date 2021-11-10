#Demo: Adding functions to class
#Concept #1 : Class Variable shared by all objects of class. Here "personCount"
#This program gives the number of Person objects created
#Concept #2 : __variablename will create a "secret" variable shared by all objects. Used for "Data Hiding"
class Person:
  __secretCount = 0;
  personCount = 0
  def __init__(self,name,age):
    self.name = name;
    self.age = age;
    Person.personCount = Person.personCount + 1
    self.__secretCount = self.__secretCount + 1

  def display(self):
        print("\nName of Person  is", self.name)
        print("\nAge of Person  is", self.age)
        print("personCount: The Total number of person objects is %d" %self.personCount)
        print("__secretCount: The Total number of person objects is %d" %self.__secretCount)

p1 = Person("Leonardo de Caprio", 26)
p2 = Person("Kate Winslet", 24)
p1.display()
print("Displays 'personCount' because it is public")
print("personCount: The Total number of person objects is %d" %Person.personCount)
print("__secretCount: The Total number of person objects is %d" %Person.__secretCount) #Will give Error
