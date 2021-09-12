# Task 1.1
# Write a Python program to calculate the length of a string without using the `len` function.

# User inputs the string
string = str(input())
# counter for characters in a string
count = 0
for i in string:
    count += 1
print("Length of a string: ", count)

# Task 1.2
# Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).

string = str(input())

dictionary = {}

for n in string:
    keys = dictionary.keys()
    if n in keys:
        dictionary[n] += 1
    else:
        dictionary[n] = 1
print (dictionary)

