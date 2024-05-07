import sys

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers")
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

# Verifica si se proporciona exactamente un argumento
if len(sys.argv) != 2:
    print("Usage: python script.py <number>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
    result = factorial(num)
    print(result)
except ValueError:
    print("Error: Input must be a non-negative integer")
    sys.exit(1)
