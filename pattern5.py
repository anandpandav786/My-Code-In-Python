# Program for the below pattern
# A B C D
# A B C
# A B
# A

for i in range(68, 64, -1):
    for j in range(65, i+1):
        print(chr(j), end=" ")
    print()
