#Q1= 
l = [1, 2, 3, 4, 5, 6, 7, 8]
for i, item in enumerate(l):
    if i ==2 or i ==4 or i==6:
        print(item)


#Q2=
n = int(input("Enter a number: "))
table = [n*i for i in range(1, 11)]
print(table)

#Q3=
try:
   a = int(input("Enter a number: "))
   b = int(input("Enter second number: "))
   print(a/b)

except ZeroDivisionError as v:
   print("Infinite")

