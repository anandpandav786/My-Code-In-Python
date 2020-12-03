# Program for function which will accept the number and print its square

def sq(x):
    y = x * x
    return y

a = int(input("Enter the number : "))
s = sq(a)
print("Square is : ", s)