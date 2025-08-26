# Task 1: Factorial Function

# Function to calculate factorial using loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Sample call
sample_number = 5
print(f"The factorial of {sample_number} is: {factorial(sample_number)}")
