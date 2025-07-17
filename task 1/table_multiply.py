def table_multiply ():
    x = int(input("add a number: "))

    for i in range(x+1):
        for j in range(1,i+1):
         print(f"{j}x{i} = {j*i} ")

table_multiply()