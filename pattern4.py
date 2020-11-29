# Program for the following pattern
# A
# A B
# A B C
# A B C D

for i in range(65, 69):
    for j in range(65, i+1):
        print(chr(j), end=" ")
    print()
