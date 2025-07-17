def mario ():
        
    stars =int(input("Enter the number of starts: "))
    for i in range(stars +1):
        print(" " * (stars - i) ,i * "*")



def pyramid2():    
    x=[' ',' ', ' ',' ',' ']

    for i in range (1,6):
        x.append('*')
        x.remove(' ')
        print(x)        