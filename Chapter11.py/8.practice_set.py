#Q1= 
class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("BHow Bhow!")


d = Dog()

d.bark()




#Q2

class Employee:
    salary = 4564
    increment = 4784768749

e =Employee()
# e.salary()
# e.increment()
print(e.salary, e.increment)