from array import *

a = array('i', [])
n = int(input("Enter the number of elements you want : "))

for i in range(n):
    x = int(input("Enter the number :"))
    a.append(x)

for i in range(n):
    print(a[i])

val= int(input("Enter the number to search : "))

for i in range(n):
    if val == a[i] :
        print("Number found ")
        break
else:
    print("Number not found ")