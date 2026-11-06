a = int(input("Enter a number: "))
b = int(input("Enter second number: "))

if(b==0):
    raise ZeroDivisionError("hey our program is not meant to divivde number by zero")
else:
    print(f"The devision a/b is {a/b}")