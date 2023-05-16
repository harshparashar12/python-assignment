num = int(input("Enter a number: "))
prime_factors = []
for i in range(2, num+1):
while num % i == 0:
prime_factors.append(i)
num //= i
if num == 1:
break
print(f"The prime factors of {num} are: {prime_factors}")
