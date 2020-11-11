num = int(input("Enter the number : "))

for i in range(1,num):
    if num % i == 0 :
        print("Not Prime ")
        break
else:
    print("Prime")