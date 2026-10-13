#Q1 = Write a program to create a dictionary of Hindi words with values as their english translatio. Provide user with an option to look it up!
words = {
    "maddad":"help",
    "kursi":"chair",
    "doodh":"milk",
    "pankha":"fan"
}
word = input("Enter the world you want meaning of: ")

print(words[word])

#Q2 = Write a program to input eight numbers from the user and display all the unique numbers(once).
s = set()
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))
n = input("Enter number : ")
s.add(int(n))

print(s)

#Q3 = Can we have a set with 18(int) and '18' (str) as a value in it?
s = set()
s.add(18)
s.add("18")
print(s)


#Q4= s ={}  What is the type of's'?
# Ans = Dictionary

s={}
type(s)

#Q5 = Change the given code
s = {8, 7, 12, "Harry", [1,2]}
# ans = NO ww can"t change