num = int(input("Enter a number: "))
product_of_digits = 1
temp = num
while temp > 0:
digit = temp % 10
product_of_digits *= digit
temp //= 10
print(f"Product of digits of {num}: {product_of_digits}")