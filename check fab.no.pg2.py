n = int(input("Enter a number: "))
a, b = 0, 1
fib = 0
while fib < n:
fib = a + b
a, b = b, fib
if fib == n:
print(f"{n} is a Fibonacci number.")
break
else:
print(f"{n} is not a Fibonacci number.")
