# Q1. Write a python program to display a user entered name followed by good afternoon using input function.
name = input("Enter your name: ")
print(f"Good Afternoon {name} ")


#Q2. Write a program to detect double space in a string
name = "Harry is a good  boy and"
print(name.find("  "))

#Q3. REplace the double space from 3 with single spaces.
name = "Harry is a good  boy and"
print(name.replace("  ", " "))


#Q4. Writea program to format the following using escape sequence letter characters.
letter = "dear ad\nfk\tl"
print(letter)