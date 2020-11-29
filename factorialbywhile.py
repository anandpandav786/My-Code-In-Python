# Program to print the factorial of a number

x = int(input("Enter any number : "))
i = 1
fact = 1
while i <= x:
    fact = fact * i
    i = i + 1
print("Factorial of ", x, " is : ", fact)
