# Program for function which will accept the list and print its square


def sq(list):
    t1 = []
    for x in list:
        y = x * x
        t1.append(y)
    return t1


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = sq(list1)
print(list2)
