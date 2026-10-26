#Q1 = Write a program using functions to find greatest of three numbers.
a=1
b=54
c=3
def greatest(a, b, c):
    if(a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b 
    elif(c>b and c>a):
        return c 
    
print(greatest(a, b, c))


#Q2= Write a python program using functions to convert celsius to farahneit
def f_to_c(f):
    return 5*(f-32)/9

f= int(input("Enter temperature in F: "))
print(f_to_c(f))


#Q3 Write a program to find sum of n natural number using recursion.
def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
n=int(input("Enter a number: "))
print(sum(n))

#Q4= Write a program to convert to inches to cm
def inch_to_cms(inch):
    return inch * 2.54
n=int(input("Enter a number: "))
print(f"The corresponding value in cm is {inch_to_cms(n)}")