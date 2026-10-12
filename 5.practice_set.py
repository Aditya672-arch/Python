#Q1. Write a program to store seven fruits in a list entered by the user
fruits = []

f1 = input("enter fruit name: ")
f2 = input("enter fruit name: ")
f3 = input("enter fruit name: ")
f4 = input("enter fruit name: ")
f5 = input("enter fruit name: ")
f6 = input("enter fruit name: ")
f7 = input("enter fruit name: ")
fruits.append(f1)
fruits.append(f2)
fruits.append(f3)
fruits.append(f4)
fruits.append(f5)
fruits.append(f6)
fruits.append(f7)
print(fruits)


#Q2. Write a program to accept marks of 6 students and display them in a stored manner.

marks = []

f1 = int(input("enter marks here : "))
f2 = int(input("enter marks here : "))
f3 = int(input("enter marks here : "))
f4 = int(input("enter marks here : "))
f5 = int(input("enter marks here : "))
f6 = int(input("enter marks here : "))
marks.append(f1)
marks.append(f2)
marks.append(f3)
marks.append(f4)
marks.append(f5)
marks.append(f6)
marks.sort()
print(marks)


#Q3.Check that a tuple type cannot be changed in a python.

a = (34, 48, "Harry")
a[2] = "Harrybrook"


#Q4. Write a program to sum a  list with 4 numbers
l = [34, 48, 64, 78]
print(sum(l))

#Q5. Write a program to count the number of zeroea in the following tuple:
a = ( 7, 0, 8, 0, 0, 9)
n= a.count(0)
print(n)