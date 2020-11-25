def game(n,m,y):
    list1=[i for i in range(1,n+1)]
    list1
    while len(list1)>y:
        list1.remove(list1[m-1])
        i=0
        while i<m-1:
            list1.append(list1[0])
            list1.remove(list1[0])
            i=i+1
    list1        
    return list1