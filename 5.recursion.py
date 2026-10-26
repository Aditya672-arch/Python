'''
factorial(1) = 1
factorial(2) = 1X2
factorial(3) = 1X2X3
factorial(4) = 1X2X3X4
factorial(5) = 1X2X3X4X5
factorial(n) = n X n-1 X.......3X2X1


factorial(n) = n*factorial(n-1)
'''
def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)
n= int(input("Enter a number: "))
print(f"The factorial of this number is: {factorial(n)}")