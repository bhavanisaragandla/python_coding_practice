# 1. REVERSE A STRING


string = input("Enter a string: ")

reverse = string[::-1]

print("Reversed string:", reverse)



# 2. CHECK WHETHER A STRING IS PALINDROME


string = input("Enter a string: ")

reverse = string[::-1]

if string == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")



# 3. COUNT VOWELS AND CONSONANTS


string = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in string:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)


# 4. COUNT THE NUMBER OF WORDS IN A STRING


string = input("Enter a string: ")

words = string.split()

print("Number of words:", len(words))


# 5. CONVERT LOWERCASE LETTERS TO UPPERCASE
#    WITHOUT USING .upper()

string = input("Enter a lowercase string: ")

result = ""

for ch in string:
    if 'a' <= ch <= 'z':
        # Convert lowercase ASCII value to uppercase
        result += chr(ord(ch) - 32)
    else:
        result += ch

print("Uppercase string:", result)