input_string = input("Enter a string: ")
duplicates = []
for char in input_string:
if input_string.count(char) > 1:
if char not in duplicates:
duplicates.append(char)
print("Original string:", input_string)
print("Duplicate characters:", duplicates)