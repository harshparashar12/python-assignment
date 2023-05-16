input_string = input("Enter a string: ")
output_string = ""
for i in range(len(input_string)):
if input_string[i] not in input_string[:i]:
output_string += input_string[i]
print("Original string:", input_string)
print("Modified string:", output_string)