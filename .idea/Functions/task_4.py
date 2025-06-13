def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

def fibonacci(n):
    if n ==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n - 2)

print("Factorial of 5 is",factorial(5),end=". ")
print("The 6th Fibonacci number is",fibonacci(6), end=".")