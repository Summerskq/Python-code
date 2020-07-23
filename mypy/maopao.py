list=[3,5,6,32,5,6,2,35,65,22]
def bubble(list1):
    for i in range(len(list1)):
        for j in range(len(list1)-1-i):
            if list1[j+1]<list1[j]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
    print(list1)
bubble(list)
