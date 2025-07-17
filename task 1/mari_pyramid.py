def mario ():
        
    stars =int(input("Enter the number of starts: "))
    for i in range(stars +1):
        print(" " * (stars - i) ,i * "*")

mario()