
# 1. Write a function to check whether a number is prime
# Question: Create a function that returns True if a number is prime.

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


print("1.", is_prime(17))


# ============================================================

# 2. Write a function to calculate factorial
# Question: Create a function to find the factorial of a number.

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


print("2. Factorial:", factorial(5))


# ============================================================

# 3. Write a function to calculate mean of a list
# Question: Create a function that returns the average of a list.

def calculate_mean(numbers):
    total = 0

    for num in numbers:
        total += num

    return total / len(numbers)


numbers = [10, 20, 30, 40, 50]

print("3. Mean:", calculate_mean(numbers))


# ============================================================

# 4. Write a function that accepts any number of arguments
# Question: Use *args to calculate the sum of any number of values.

def calculate_sum(*args):
    total = 0

    for num in args:
        total += num

    return total


print("4. Sum:", calculate_sum(10, 20, 30, 40))


# ============================================================

# 5. Write a function using *args and **kwargs
# Question: Create a function that accepts multiple values
# and keyword arguments.

def student_details(*args, **kwargs):

    print("Subjects:", args)
    print("Details:", kwargs)


student_details(
    "Python",
    "SQL",
    "Statistics",
    name="Bhavani",
    year=3,
    branch="CSE"
)

# LAMBDA & COMPREHENSIONS
# ============================================================


# 1. Use lambda to add 10 to each number in a list
# Question: Add 10 to every element using lambda and map().

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x + 10, numbers))

print("1. Add 10:", result)


# ============================================================

# 2. Use map() to square all numbers
# Question: Find the square of every number using map().

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print("2. Squares:", squares)


# ============================================================

# 3. Use filter() to find even numbers
# Question: Extract only even numbers using filter().

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("3. Even numbers:", even_numbers)


# ============================================================

# 4. Create a dictionary using dictionary comprehension
# Question: Create a dictionary containing numbers and their squares.

numbers = [1, 2, 3, 4, 5]

squares = {x: x ** 2 for x in numbers}

print("4. Dictionary:", squares)


# ============================================================

# 5. Create a list of cubes using list comprehension
# Question: Create a list containing cubes from 1 to 10.

cubes = [x ** 3 for x in range(1, 11)]

print("5. Cubes:", cubes)

# ============================================================



# 1. Find the second most frequent character
# Question: Find the character with the second-highest frequency.

text = "programming"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

sorted_frequency = sorted(
    frequency.items(),
    key=lambda x: x[1],
    reverse=True
)

second_most_frequent = sorted_frequency[1]

print("1. Second most frequent character:",
      second_most_frequent)


# ============================================================

# 2. Find words appearing more than once
# Question: Find duplicate words in a sentence.

sentence = "python is easy and python is powerful"

words = sentence.lower().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

duplicates = []

for word, count in frequency.items():
    if count > 1:
        duplicates.append(word)

print("2. Repeated words:", duplicates)


# ============================================================

# 3. Convert a nested dictionary into a flat dictionary
# Question:
# Convert:
# {"student": {"name": "Bhavani", "age": 20}}
#
# Into:
# {"student_name": "Bhavani", "student_age": 20}

nested = {
    "student": {
        "name": "Bhavani",
        "age": 20
    }
}

flat = {}

for outer_key, inner_dict in nested.items():
    for inner_key, value in inner_dict.items():
        new_key = outer_key + "_" + inner_key
        flat[new_key] = value

print("3. Flat dictionary:", flat)


# ============================================================

# 4. Sort a list of dictionaries by a specific key
# Question: Sort students by their marks.

students = [
    {"name": "Asha", "marks": 75},
    {"name": "Ravi", "marks": 90},
    {"name": "Priya", "marks": 82},
    {"name": "Arun", "marks": 68}
]

sorted_students = sorted(
    students,
    key=lambda x: x["marks"]
)

print("4. Sorted students:")

for student in sorted_students:
    print(student)


# ============================================================

# 5. Find missing values in a list of numbers
# Question: Find missing numbers from 1 to n.

numbers = [1, 2, 3, 5, 6, 8, 10]

n = 10

missing = []

for i in range(1, n + 1):
    if i not in numbers:
        missing.append(i)

print("5. Missing numbers:", missing)