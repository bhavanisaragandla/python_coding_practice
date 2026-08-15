#check whether a number is prime
n = int(input("Enter a number"))
if n <= 1:
    print("Not a prime number")
else:    
    is_prime = True
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime number")  
    else:
        print("Not a Prime Number")

#print prime numbers in a range
start = int(input("Enter starting number"))
End = int(input("Enter ending number"))
for n in range(start,End+1):
    if n<2:
        continue
    is_prime = True
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            is_prime = False 
            break
    if is_prime:
        print(n) 

#Find factors of a number
n = int(input("Enter a number: "))

print("Factors:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i)

# Find GCD of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD:", gcd)


#Find LCM of Two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(max(a, b), a * b + 1):
    if i % a == 0 and i % b == 0:
        lcm = i
        break

print("LCM:", lcm)