def email_validation (x):                        
        
    list = x.split("@")
    if "." in list[1][-1]:
        return False
    elif "." in list[1][0]:
        return False
    elif not list[0]:
        return False       
    else:
        return True
    
email = input("Enter you email: ")

if email_validation(email) is True:
    print("Your email is valid")
else:
    print("Your email is not valid")