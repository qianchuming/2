list1=[i for i in range(1,31)]
list1
while len(list1)>2:
    list1.remove(list1[2])
    list1.append(list1[0])
    list1.append(list1[1])
    list1.remove(list1[0])
    list1.remove(list1[0])
list1