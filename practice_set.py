name = input("Enter name: ")
marks= input("Enter marks: ")
phone = input("Enter phone: ")

s = "The name is {}, marks{}, phone number{}".format(name, marks, phone)
print(s)


#Q2
table = [str(7*i) for i in range(1, 11)]
s = "\n".join(table)
print(s) 