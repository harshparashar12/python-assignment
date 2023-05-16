input_string = input("Enter a string: ")
char_count = {}
for char in input_string:
if char in char_count:
char_count[char] += 1
else:
char_count[char] = 1
least_frequent_char = None
least_frequent_count = float('inf')
for char, count in char_count.items():
if count < least_frequent_count:
least_frequent_char = char
least_frequent_count = count
print(f"Least frequent character: '{least_frequent_char}'
({least_frequent_count} occurrences)")