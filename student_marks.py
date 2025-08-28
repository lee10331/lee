# Task 1: Create a Dictionary of Student Marks

# Step 1: Create dictionary
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90,
    "Ethan": 88
}

# Step 2: Ask user for input
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve marks or show error
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the dictionary.")
