def math(x, y):
    a = x + y
    s = x - y
    m = x * y
    d = x / y
    return a, s, m, d


num1 = int(input("Enter 1st numbers : "))
num2 = int(input("Enter 2nd numbers : "))
add, sub, mul, div = math(num1, num2)

print("Addition is          : ", add)
print("Subtraction is       : ", sub)
print("Multiplication is    : ", mul)
print("Division is          : ", div)
