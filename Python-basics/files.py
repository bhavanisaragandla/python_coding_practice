# ============================================================
# - FILES
# ============================================================

# 1. Read a text file
# Question: Read and display the contents of a text file.

with open("data.txt", "r") as file:
    content = file.read()

print("1. File contents:")
print(content)


# ============================================================

# 2. Count total lines in a file
# Question: Count how many lines are present in a text file.

with open("data.txt", "r") as file:
    lines = file.readlines()

print("2. Total lines:", len(lines))


# ============================================================

# 3. Count total words in a file
# Question: Count the total number of words in a text file.

with open("data.txt", "r") as file:
    content = file.read()

words = content.split()

print("3. Total words:", len(words))


# ============================================================

# 4. Find the longest line in a file
# Question: Find the line containing the maximum number of characters.

with open("data.txt", "r") as file:
    lines = file.readlines()

longest_line = max(lines, key=len)

print("4. Longest line:")
print(longest_line.strip())


# ============================================================

# 5. Find the most frequent word in a file
# Question: Find the word that appears most frequently.

with open("data.txt", "r") as file:
    content = file.read().lower()

words = content.split()

frequency = {}

for word in words:
    word = word.strip(".,!?;:")

    frequency[word] = frequency.get(word, 0) + 1

most_frequent = max(frequency, key=frequency.get)

print("5. Most frequent word:", most_frequent)
print("   Frequency:", frequency[most_frequent])


# ============================================================
# DAY 17 - CSV
# ============================================================

import csv


# 1. Read a CSV file using Python
# Question: Read and display every row from a CSV file.

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    print("1. CSV Data:")

    for row in reader:
        print(row)


# ============================================================

# 2. Calculate the average of a numeric column
# Question: Find the average Marks of all students.

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    marks = []

    for row in reader:
        marks.append(float(row["Marks"]))

average = sum(marks) / len(marks)

print("2. Average Marks:", average)


# ============================================================

# 3. Find the row with the maximum value in a column
# Question: Find the student who has the highest marks.

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    rows = list(reader)

highest = max(rows, key=lambda row: float(row["Marks"]))

print("3. Highest Marks:")
print(highest)


# ============================================================

# 4. Filter rows based on a condition
# Question: Display students whose marks are greater than 80.

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    print("4. Students with Marks > 80:")

    for row in reader:
        if float(row["Marks"]) > 80:
            print(row)


# ============================================================

# 5. Write filtered data to a new CSV file
# Question: Create a new CSV containing only students
# whose marks are greater than 80.

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    filtered_rows = []

    for row in reader:
        if float(row["Marks"]) > 80:
            filtered_rows.append(row)


with open("high_scorers.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "Marks", "City"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(filtered_rows)

print("5. Filtered data saved to high_scorers.csv")


# ============================================================
#  EXCEPTION HANDLING
# ============================================================


# 1. Create a calculator with error handling
# Question: Create a calculator that handles invalid input.

try:
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        result = num1 / num2

    else:
        raise ValueError("Invalid operator")

    print("1. Result:", result)

except ValueError as e:
    print("Error:", e)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")


# ============================================================

# 2. Handle invalid integer input
# Question: Ask the user for an integer and handle invalid input.

try:
    number = int(input("Enter an integer: "))
    print("2. You entered:", number)

except ValueError:
    print("2. Error: Please enter a valid integer.")


# ============================================================

# 3. Handle division by zero
# Question: Divide two numbers and handle ZeroDivisionError.

try:
    a = 10
    b = 0

    result = a / b

    print("3. Result:", result)

except ZeroDivisionError:
    print("3. Error: Division by zero is not allowed.")


# ============================================================

# 4. Handle file not found error
# Question: Try to read a file that may not exist.

try:
    with open("unknown.txt", "r") as file:
        content = file.read()

    print("4. File contents:")
    print(content)

except FileNotFoundError:
    print("4. Error: File not found.")


# ============================================================

# 5. Create a custom exception for invalid age
# Question: Create an exception if the entered age is invalid.

class InvalidAgeError(Exception):
    pass


try:
    age = int(input("Enter your age: "))

    if age < 0 or age > 120:
        raise InvalidAgeError("Age must be between 0 and 120.")

    print("5. Valid age:", age)

except InvalidAgeError as e:
    print("5. Error:", e)

except ValueError:
    print("5. Error: Please enter a valid number.")