import re
def has_special_char(s):
pattern = re.compile(r'\W')
return bool(pattern.search(s))
input_string = input("Enter a string: ")
if has_special_char(input_string):
print("The string contains a special character.")
else:
print("The string does not contain any special character.")