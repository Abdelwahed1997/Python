def vowels_check():
   
    vowels = "aeiou"
    x = input("Enter a word:  ")
    count = 0
    for i in x:
        if i in vowels:
            count += 1
    print(count)
    return True

vowels_check()