# Task 2: Using the Math Module for Calculations
import math

# Taking user input
num = float(input("Enter a number: "))

# Calculations using math module
square_root = math.sqrt(num)
natural_log = math.log(num) if num > 0 else "Undefined (log of non-positive number)"
sine_value = math.sin(num)

# Display results
print(f"Square root of {num} is: {square_root}")
print(f"Natural logarithm of {num} is: {natural_log}")
print(f"Sine of {num} radians is: {sine_value}")
