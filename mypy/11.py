list1 = [1, 2, 3]
list2 = [2,3,5,6]
list = []
for i in list1:
    if i not in list2:
        list.append(i)
for i in list2:
    if i not in list1:
        list.append(i)
print(list)
print ([i for i in list1 if i in list2])