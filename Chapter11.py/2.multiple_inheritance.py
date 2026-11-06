class Employee:
    company = "ITC"
    salary = 1400000
    def show(self):
        print(f"The name of the employee is {self.company} and the salary is: {self.salary}")


class Coder:
    language = "python"
    def printlanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")


class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.printlanguages()
b.showLanguage