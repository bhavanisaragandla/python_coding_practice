# Reverse a string 
text = input("Enter a string:")
reverse = text[::-1]
print("Reverse string:",reverse)

# count digits in a number
n = int(input("Enter a number:"))
count = 0
while n > 0:
    n//=10
    count+=1
print("Count :",count)  

# sum of digits in a number
n = int(input("Enter a number:"))
sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n//=10
print("Sum of digits:",sum)  

# check whether a number is a palindrome or not
n = int(input("Enter n value:"))
original = n
reverse = 0
while n > 0 :
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10
if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")  

# Argstrong Number
n = int(input("Enter a number"))
original = n
digits=len(str(n))
total = 0
while n > 0:
    digit = n %10
    total += digit ** digits
    n //= 10
if total == original :
    print("Argstone")
else:
    print("Not Argstone")