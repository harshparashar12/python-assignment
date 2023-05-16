num = int(input("Enter a number: "))
sum_of_digits = 0
temp = num
while temp > 0:
digit = temp % 10
sum_of_digits += digit
temp //= 10
print(f"Sum of digits of {num}: {sum_of_digits}")