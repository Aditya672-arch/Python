#Q1. Write a program to find the greatest of four numbers entered by the user.
a1 = int(input("Enter the number: "))
a2 = int(input("Enter the number: "))
a3 = int(input("Enter the number: "))
a4 = int(input("Enter the number: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1:", a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a2:", a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is a3:", a3)
elif(a4>a1 and a4>a2 and a4>a3):
    print("Greatest number is a4:", a4)



#Q2.Make a spam call setect program
p1= "Make a lot of money" 
p2 = "buy now"
p3= "Subscribe this"
p4= "click this"

message = input("Enter your message: ")
if((p1 in message) or (p2 in message )or(p3 in message) or (p4 in message)):
    print("This message is spam")

else:
    print("This message  is not a  spam")

#Q3. 
username = input("Enter username: ")

if(len(username)<10):
    print("your username contains less than 10 characters")

else:
    print("All is well:  !")


#Q4. 
l = ["Harry", "Aditya ", "MOhan"]
name = input("Enter your name: ")
if(name in l):
    print("Your name is in the list: ")

else:
    print("Name not exists: ")