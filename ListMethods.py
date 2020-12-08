#Using different Methods with the list

mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(mylist)

#Append
print("==Append=======")
mylist.append(100)
print(mylist)

#Insert
print("==Insert=======")
mylist.insert(1,100)
print(mylist)

#Extend
print("==Extend=======")
mylist.extend([101, 102, 103])
print(mylist)

#Remove
print("==Remove=======")
mylist.remove(100)
print(mylist)

#POP
print("==POP=======")
mylist.pop(3)
print(mylist)

#Index
print("==Remove=======")
x = mylist.index(100)
print(x)

#Count
print("==Count=======")
x = mylist.count(100)
print(x)

#Sort
print("==Sort=======")
mylist.sort()
print(x)

#Reverse Sort
print("==Reversew Sort=======")
mylist.sort(reverse=True)
print(x)

#Reference(Pointing to same memory location)
print("==Reference=======")
mylist1 = mylist
mylist.remove(20)
print(mylist)
print(mylist1)

#Making the another copy of the list
print("==Copy=======")
mylist1 = mylist.copy()
mylist.remove(30)
print(mylist)
print(mylist1)

#clear
mylist.clear()
print(mylist)