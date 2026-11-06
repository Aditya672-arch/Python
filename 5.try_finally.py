try:
    a = int(input("Hey, Enter a number: "))
    print(a)


except Exception as e:
   print(e)

finally:
   print("Thank you") #finally always written if code is correct or incorrect     