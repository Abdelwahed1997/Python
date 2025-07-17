def multiplier2():
    list=[]
    x = int(input("enter a number : "))
    for i in range(x+1):
        temp=[]
        for j in range(1,i+1) :
            
            temp.append(j*i)
        list.append(temp)
    print(list)

multiplier2()