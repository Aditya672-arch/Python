#Q1= Creating a class "Programmer" for storing information of few programmers working at microsoft.
class Programmer:
    Age = 22
    Work = "Microsoft developer"
    language = "Python"
    shift = "Work from home"


Harry = Programmer
Harry.name  = "Harry"
print(Harry.Age,Harry.name, Harry.shift)

Amit = Programmer 
Amit.name  = "Amit"
print(Amit.Work, Amit.name)




#Q2= Write a class "calculator " capable of inding square, cube and square root of a number.
class calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"The square is: {self.n*self.n}")

    def cube(self):
        print(f"The cube is: {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The square root is: {self.n**1/2}")



a = calculator(4)
a.square()
a.cube()
a.squareroot()


#Q3= Add a static m,ethod in problem2, to greet the user with helo.
class calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"The square is: {self.n*self.n}")
  
    def cube(self):
        print(f"The cube is: {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The square root is: {self.n**1/2}")

    @staticmethod
    def hello():
        print("Hello! How are you.")

a = calculator(4)
a.square()
a.cube()
a.squareroot()
a.hello()


#Write a class Train which has methods to book a ticket, get status(no. of seats) and get fare information of
# a train running under Indian Railways.

from random import randint

class Train:

    def __init__(self,trainNO):
        self.trainNo = trainNO

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getfare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from{fro} to {to} is {randint(222, 54545)}")


t = Train(4551541)
t.book("Rampur", "delhi")
t.getStatus()
t.getfare("Rampur", "Delhi")