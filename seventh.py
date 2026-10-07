print("Program to find maximum elements in an array")


arr = [12, 45,7, 89, 347, 22]
max_element = arr[0]
for num in arr:
    if num > max_element:
        max_element = num
print("Maximum element in the array is:", max_element)