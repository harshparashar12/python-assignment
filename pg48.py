 input_string = input("Enter a string: ")
n = int(input("Enter the number of positions to rotate the
string: "))
part1 = input_string[n:]
part2 = input_string[:n]
rotated_string = part1 + part2
print("Original string:", input_string)
print("Rotated string:", rotated_string)