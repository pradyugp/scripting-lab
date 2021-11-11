class Person:
    personCount = 0
    __secretCount = 0
    def __init__(self,name,age):
        self.name = name;
        self.age = age;
        Person.personCount = Person.personCount + 1
        self.__secretCount = self.__secretCount + 1

    def display(self):
        print("\n Name of Person is ", self.name)
        print("\n Age of Person is ", self.age)
        print("PersonCount: the number of person objects is %d" %self.personCount)
        print("__secretCount: the number of secret objects is %d" %self.__secretCount)



p1 = Person("Tintin", 23)
p2 = Person("Haddock", 45)
p1.display()
p2.display()
print("person count is %d" %Person.personCount)
print("secret count is %d" %Person.__secretCount)

        

