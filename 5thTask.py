# Task 5: Calculate the Factorial of a Number

n = int(input("Enter a number:-"))

factorial = 1

for i in range (1,n+1):
    factorial *=i
print(factorial)
