# Label the program written in problem 4 with comments
import os

# os.environ behaves like a dictionary of environment variables
env_vars = os.environ

# Loop through items and print key: value
for key, value in env_vars.items():
    print(f"{key}: {value}")
my_dict = {"name": "Alice", "age": 25, "city": "Indore"}

# Print each key/value
for key, value in my_dict.items():
    print(key, ":", value)