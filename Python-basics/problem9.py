# 1. Find the largest element in a list
# Question: Find the largest number without using max().

numbers = [10, 25, 7, 45, 18]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("1. Largest:", largest)


# 2. Find the smallest element in a list
# Question: Find the smallest number without using min().

numbers = [10, 25, 7, 45, 18]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("2. Smallest:", smallest)



# 3. Calculate the sum of all elements
# Question: Find the sum of all numbers without using sum().

numbers = [10, 20, 30, 40, 50]

total = 0

for num in numbers:
    total += num

print("3. Sum:", total)



# 4. Remove duplicate elements
# Question: Remove duplicate values from a list.

numbers = [10, 20, 10, 30, 20, 40, 30]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("4. Without duplicates:", unique)




# 5. Reverse a list without using reverse()
# Question: Reverse the elements of a list.

numbers = [1, 2, 3, 4, 5]

reversed_list = []

for i in range(len(numbers) - 1, -1, -1):
    reversed_list.append(numbers[i])

print("5. Reversed:", reversed_list)



# 6. Find the second-largest element
# Question: Find the second-largest number in a list.

numbers = [10, 50, 20, 40, 30]

unique_numbers = list(set(numbers))
unique_numbers.sort()

second_largest = unique_numbers[-2]

print("6. Second largest:", second_largest)



# 7. Find duplicate elements
# Question: Find all elements that appear more than once.

numbers = [10, 20, 10, 30, 40, 20, 50, 30]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("7. Duplicates:", duplicates)



# 8. Find common elements between two lists
# Question: Find elements that are present in both lists.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = []

for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print("8. Common elements:", common)




# 9. Separate even and odd numbers
# Question: Create two lists containing even and odd numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("9. Even numbers:", even)
print("   Odd numbers:", odd)



# 10. Flatten a nested list
# Question: Convert a nested list into a single list.

nested = [[1, 2], [3, 4], [5, 6]]

flat = []

for sublist in nested:
    for num in sublist:
        flat.append(num)

print("10. Flattened list:", flat)