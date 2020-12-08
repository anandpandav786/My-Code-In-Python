#Printing the even number using filter in lambda function

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = list(filter(lambda x:x % 2 == 0, list1))
print(list2)