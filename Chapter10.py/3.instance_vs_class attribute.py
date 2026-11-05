class Employee:
    age = 28  #attributes
    language = "Py"  #class attributes
    salary = 100000  #attributes



Mohan = Employee()  #Mohan is a object
Mohan.language = "javascript" #instance attributes
print(Mohan.language, Mohan.salary)


''' 
Instance attributes take preference over class attributes.
'''