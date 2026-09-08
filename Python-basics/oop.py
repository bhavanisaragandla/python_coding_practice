# ============================================================
# OOP
# ============================================================


# 1. Create a Student class with attributes
# Question: Create a Student class with name, age and course.

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)


student = Student("Bhavani", 20, "B.Tech CSE")

print("DAY 19 - Q1")
student.display()


# ============================================================

# 2. Create an Employee class with salary details
# Question: Create an Employee class with name, salary and department.

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Department:", self.department)


employee = Employee("Ravi", 50000, "IT")

print("\nDAY 19 - Q2")
employee.display()


# ============================================================

# 3. Create a BankAccount class
# Question: Create a BankAccount class with account holder
# and balance.

class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def display(self):
        print("Account Holder:", self.holder)
        print("Balance:", self.balance)


account = BankAccount("Bhavani", 10000)

print("\nDAY 19 - Q3")
account.display()


# ============================================================

# 4. Implement deposit and withdraw methods
# Question: Add deposit() and withdraw() methods to BankAccount.

class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Current Balance:", self.balance)


account = BankAccount("Bhavani", 10000)

print("\nDAY 19 - Q4")

account.deposit(5000)
account.withdraw(3000)
account.display_balance()


# ============================================================

# 5. Calculate student grade using a class
# Question: Create a class that calculates grade based on marks.

class StudentGrade:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 60:
            return "D"
        else:
            return "F"


student = StudentGrade("Bhavani", 85)

print("\nDAY 19 - Q5")
print("Student:", student.name)
print("Marks:", student.marks)
print("Grade:", student.calculate_grade())


# ============================================================
# DAY 20 - OOP
# ============================================================


# 1. Implement inheritance
# Question: Create a parent class and inherit it into a child class.

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog = Dog()

print("\nDAY 20 - Q1")
dog.eat()
dog.bark()


# ============================================================

# 2. Implement method overriding
# Question: Override a parent class method in the child class.

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


dog = Dog()

print("\nDAY 20 - Q2")
dog.sound()


# ============================================================

# 3. Implement encapsulation
# Question: Make a balance variable private.

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount


account = BankAccount(10000)

print("\nDAY 20 - Q3")
print("Balance:", account.get_balance())

account.deposit(5000)

print("After deposit:", account.get_balance())


# ============================================================

# 4. Create a class using @property
# Question: Use @property to control access to an attribute.

class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value:
            self._name = value
        else:
            print("Name cannot be empty")


student = Student("Bhavani")

print("\nDAY 20 - Q4")
print("Name:", student.name)

student.name = "Ravi"
print("Updated Name:", student.name)


# ============================================================

# 5. Class variable and instance variable
# Question: Create a class with one class variable and
# one instance variable.

class Student:

    college = "ABC Engineering College"   # Class variable

    def __init__(self, name):
        self.name = name                  # Instance variable


student1 = Student("Bhavani")
student2 = Student("Ravi")

print("\nDAY 20 - Q5")

print("Student 1:", student1.name)
print("College:", student1.college)

print("Student 2:", student2.name)
print("College:", student2.college)


# ============================================================
# DATE & TIME
# ============================================================

from datetime import datetime, date


# 1. Calculate age from date of birth
# Question: Calculate a person's current age.

dob = date(2005, 5, 15)
today = date.today()

age = today.year - dob.year

if (today.month, today.day) < (dob.month, dob.day):
    age -= 1

print("\nDAY 21 - Q1")
print("Age:", age)


# ============================================================

# 2. Find number of days between two dates
# Question: Calculate the number of days between two dates.

date1 = date(2026, 1, 1)
date2 = date(2026, 9, 8)

difference = date2 - date1

print("\nDAY 21 - Q2")
print("Number of days:", difference.days)


# ============================================================

# 3. Find day of the week for a given date
# Question: Find which day of the week a date falls on.

given_date = date(2026, 9, 8)

day = given_date.strftime("%A")

print("\nDAY 21 - Q3")
print("Day:", day)


# ============================================================

# 4. Calculate working days between two dates
# Question: Count weekdays (Monday-Friday) between two dates.

start_date = date(2026, 9, 1)
end_date = date(2026, 9, 8)

working_days = 0
current_date = start_date

while current_date <= end_date:

    if current_date.weekday() < 5:
        working_days += 1

    current_date = current_date.replace(
        day=current_date.day + 1
    )


print("\nDAY 21 - Q4")
print("Working days:", working_days)


# ============================================================

# 5. Convert a date string into a datetime object
# Question: Convert "08-09-2026" into a datetime object.

date_string = "08-09-2026"

date_object = datetime.strptime(
    date_string,
    "%d-%m-%Y"
)

print("\nDAY 21 - Q5")
print("Datetime object:", date_object)


# ============================================================
# JSON & APIs
# ============================================================

import json


# 1. Convert a Python dictionary to JSON
# Question: Convert a dictionary into a JSON string.

student = {
    "name": "Bhavani",
    "age": 20,
    "course": "B.Tech"
}

json_data = json.dumps(student, indent=4)

print("\nDAY 22 - Q1")
print(json_data)


# ============================================================

# 2. Read JSON data from a file
# Question: Read JSON data stored in student.json.
#
# Create student.json like:
#
# {
#     "name": "Bhavani",
#     "age": 20,
#     "course": "B.Tech"
# }

try:
    with open("student.json", "r") as file:
        data = json.load(file)

    print("\nDAY 22 - Q2")
    print(data)

except FileNotFoundError:
    print("\nDAY 22 - Q2")
    print("student.json file not found")


# ============================================================

# 3. Extract nested JSON values
# Question: Extract values from nested JSON data.

data = {
    "student": {
        "name": "Bhavani",
        "course": "CSE",
        "address": {
            "city": "Hyderabad",
            "state": "Telangana"
        }
    }
}

name = data["student"]["name"]
city = data["student"]["address"]["city"]

print("\nDAY 22 - Q3")
print("Name:", name)
print("City:", city)


# ============================================================

# 4. Convert JSON to Python dictionary
# Question: Convert a JSON string into a Python dictionary.

json_string = '''
{
    "name": "Bhavani",
    "age": 20,
    "skills": ["Python", "SQL", "Power BI"]
}
'''

python_dict = json.loads(json_string)

print("\nDAY 22 - Q4")
print("Python Dictionary:")
print(python_dict)

print("Name:", python_dict["name"])
print("Skills:", python_dict["skills"])


# ============================================================

# 5. Fetch data from a public API
# Question: Fetch data from a public API and display
# selected fields.

import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:

    users = response.json()

    print("\nDAY 22 - Q5")

    for user in users:
        print(
            "Name:", user["name"],
            "| Email:", user["email"],
            "| City:", user["address"]["city"]
        )

else:
    print("API request failed")


