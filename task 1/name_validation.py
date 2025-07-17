def name_validation():
    user_input = input("Enter your name: ")
    if user_input.isalpha():
        print("The name is valid, please enter your email: ")
    elif len(user_input)==0:
        print("Name cannot be empty, please try again!")    
    else:
        print("Invalid input. Please use alphabetic characters only.")

name_validation()
