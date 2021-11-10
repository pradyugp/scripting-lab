class SLLabTest:
        name=" "
        age = 0;
        marks1 = []
        def __init__(self,age, marks1,name):
            self.age = age
            self.marks1 = marks1
            self.name = name

        def display(self):
                print(self.name)
                print(self.age)
                print(self.marks1)


listmarks = [12,14,16]
t1 = SLLabTest(18,listmarks,"XXX")
t2= SLLabTest(19,listmarks,"YYY")
t1.display()

t2.display()
