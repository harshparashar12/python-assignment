input_string = input("Enter a string: ")
delimiter = input("Enter a delimiter: ")
substring_list = input_string.split(delimiter)
output_string = delimiter.join(substring_list)
print("Original string:", input_string)
print("Substring list:", substring_list)
print("Joined string:", output_string)