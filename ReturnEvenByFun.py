# Program for the function which will accept the list of number and return the even number


def show(mylist):
    t1 = []
    for x in mylist:
        if x % 2 == 0:
            t1.append(x)
    return t1

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = show(list1)
print(list2)
