class Employee:
    name = "Mohan"  #attributes
    age = 28  #attributes
    language = "Py"  #attributes
    salary = 100000  #attributes

    def getInfo(self):
        print(f"The language is {self.language}. The salary is{self.salary}")


Mohan = Employee()  #Mohan is a object
print(Mohan.name, Mohan.salary)

Employee.getInfo(Mohan)