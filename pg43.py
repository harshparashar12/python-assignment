input_string = input("Enter a string: ")
char_count = {}
for char in input_string:
if char in char_count:
char_count[char] += 1
else:
char_count[char] = 1
max_frequency_char = None
max_frequency = 0
for char, count in char_count.items():
if count > max_frequency:
max_frequency_char = char
max_frequency = count
print(f"Character with maximum frequency:
'{max_frequency_char}' ({max_frequency} occurrences)")