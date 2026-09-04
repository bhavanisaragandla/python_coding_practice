# Problem 1: Find the first non-repeating character in a string
# Example: "aabbcde" → "c"

text = "aabbcde"

for char in text:
    if text.count(char) == 1:
        print("First non-repeating character:", char)
        break


# Problem 2: Check whether two strings are anagrams
# Example: "listen" and "silent" → Anagram

str1 = "listen"
str2 = "silent"

if len(str1) == len(str2):
    frequency1 = {}
    frequency2 = {}

    for char in str1:
        frequency1[char] = frequency1.get(char, 0) + 1

    for char in str2:
        frequency2[char] = frequency2.get(char, 0) + 1

    if frequency1 == frequency2:
        print("The strings are anagrams")
    else:
        print("The strings are not anagrams")
else:
    print("The strings are not anagrams")


# Problem 3: Find the second most frequent character
# Example: "programming" → second highest frequency character

text = "programming"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

frequencies = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

if len(frequencies) >= 2:
    print("Second most frequent character:", frequencies[1][0])
else:
    print("Second most frequent character does not exist")


# Problem 4: Reverse the order of words in a sentence
# Example: "Python is easy" → "easy is Python"

sentence = "Python is easy to learn"

words = sentence.split()

reversed_sentence = " ".join(words[::-1])

print("Reversed sentence:", reversed_sentence)


# Problem 5: Find the longest substring without repeating characters
# Example: "abcabcbb" → "abc"

text = "abcabcbb"

current = ""
longest = ""

for char in text:
    if char in current:
        current = current[current.index(char) + 1:]

    current += char

    if len(current) > len(longest):
        longest = current

print("Longest substring:", longest)


# Problem 6: Find all duplicate characters and their frequencies
# Example: "programming" → r:2, g:2, m:2

text = "programming"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Duplicate characters:")

for char, count in frequency.items():
    if count > 1:
        print(char, ":", count)


# Problem 7: Remove consecutive duplicate characters
# Example: "aaabbccdaa" → "abcda"

text = "aaabbccdaa"

result = text[0]

for char in text[1:]:
    if char != result[-1]:
        result += char

print("After removing consecutive duplicates:", result)


# Problem 8: Find the most frequent word in a sentence
# Example: "python java python c python" → python

sentence = "python java python c python"

words = sentence.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

most_frequent_word = max(frequency, key=frequency.get)

print("Most frequent word:", most_frequent_word)


# Problem 9: Count words that contain a specific character
# Example: "apple banana mango" and character "a"

sentence = "apple banana mango orange"
character = "a"

words = sentence.split()

count = 0

for word in words:
    if character in word:
        count += 1

print("Number of words containing", character, ":", count)


# Problem 10: Check whether a string is a palindrome
# Ignore spaces, special characters, and capitalization
# Example: "A man, a plan, a canal: Panama" → True

text = "A man, a plan, a canal: Panama"

cleaned_text = ""

for char in text:
    if char.isalnum():
        cleaned_text += char.lower()

if cleaned_text == cleaned_text[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")