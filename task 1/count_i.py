def i_count():
    x = input("enter a word:  ")
    count = 0
    for i in x:
        if i == "i":
            count +=1
    print(count)

i_count()