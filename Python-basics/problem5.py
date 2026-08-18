# 1. Count the frequency of each character in a string

text = "hello world"

frequency = {}

for char in text:
    if char != " ":  # Ignore spaces
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

print("1. Character Frequency:", frequency)


# 2. Remove spaces from a string

text = "Hello World Python"

# Replace spaces with nothing
no_space = text.replace(" ", "")

print("2. String without spaces:", no_space)


# 3. Remove duplicate characters from a string

text = "programming"

result = ""

for char in text:
    # Add character only if it is not already present
    if char not in result:
        result += char

print("3. After removing duplicates:", result)


# 4. Find the longest word in a sentence

sentence = "Python is a powerful programming language"

words = sentence.split()

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("4. Longest word:", longest_word)


# 5. Find the most frequent character in a string

text = "programming"

frequency = {}

for char in text:
    if char != " ":  # Ignore spaces
        frequency[char] = frequency.get(char, 0) + 1

# Find character having maximum frequency
most_frequent = max(frequency, key=frequency.get)

print("5. Most frequent character:", most_frequent)
print("   Frequency:", frequency[most_frequent])