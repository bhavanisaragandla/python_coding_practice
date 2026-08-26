# Problem 1: Count the frequency of each character in a string

text = "programming"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Character Frequency:", frequency)


# Problem 2: Remove all spaces from a string

text = "Python is easy to learn"

result = text.replace(" ", "")

print("String without spaces:", result)


# Problem 3: Remove duplicate characters from a string

text = "programming"

result = ""

for char in text:
    if char not in result:
        result += char

print("After removing duplicates:", result)


# Problem 4: Find the longest word in a sentence

sentence = "Python programming is very interesting"

words = sentence.split()

longest_word = max(words, key=len)

print("Longest word:", longest_word)


# Problem 5: Find the most frequent character in a string

text = "success"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

most_frequent = max(frequency, key=frequency.get)

print("Most frequent character:", most_frequent)