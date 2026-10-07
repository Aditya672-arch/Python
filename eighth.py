print("Write a program to count the number of vowels in a string")

text = input("Enter a srting")
vowels = 'AEIOUaeiou'
count = 0
for ch in text:
    if ch in vowels:
        count +=1
        print("Number of vowels in the string:", count)