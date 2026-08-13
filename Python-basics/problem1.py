# Check Wherther a number is even or odd
num = int(input("Enter a number"))
if num % 2 == 0:
    print("It is Even Number")
else:
    print("It is Odd Number")


# Find Largest of Three numbers
a = 25
b = 36
c = 55
if a > b and a > c:
    print(a)
elif b > a and b > c :
    print( b )
else :
    print(c)   

#Calculate Factorial
n = int(input("Enter n value:"))
factorial = 1
for i in range(1,n+1):
    factorial *= i
print("Factorial:",factorial)

#Check wherther a number a positive ,negative or zero
num = int(input("Enter value:"))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else :
    print("Zero")

#Calculate the sum of numbers from 1 to n
n = int(input("Enter n value:"))
total = 0
for i in range(1,n+1):
    total =total+i
print("sum:",total)        
