
# def name_validation(user_input):
#  if user_input.isalpha():
#     print("The User name is valid.")
#  elif len(user_input)==0:
#     print("User name cannot be empty")
    
#  else:
#      print("Invalid, please use alphabetic characters only.")
     



# def user_pass_check():
#     user = [{"name":"abdelwahed","pass":"159357"},{"name":"ali","pass":"7877"}]
#     user_input=input("enter ur name:  ")
#     for i in user:
#         if i["name"] ==user_input:
#             userPass=input("enter ur pass:  ")
#             if i["pass"] ==userPass:
#                 print("Your password is correct")
#                 break
#             else:
#                 print("Your password is incorrect")
#             break
        
#         else:
#             continue
#     else:
#         print("not found")
        

def valid_email(email):
    if '@' in email and '.' in email:
        try:
            username, domain = email.split('@')
        except ValueError:
            # More than one @ symbol
            print("Email is wrong, please try again")
            return False

        # Check if domain does not start or end with a dot
        if domain.startswith('.') or domain.endswith('.'):
            print("Email is wrong, please try again")
            return False

        if username and domain:
            if '.' in domain:
                domain_parts = domain.split('.')
                if domain_parts[0] and all(domain_parts[1:]):
                    print("Your email is correct")
                    return True
                else:
                    print("Email is wrong, please try again")
                    return False
            else:
                print("Email is wrong, please try again")
                return False
        else:
            print("Email is wrong, please try again")
            return False
    else:
        print("Email is wrong, please try again")
        return False

    

# def email_valid():
#     email = input("Enter you email: ")

#     if email_validation(email) is True:
#         print("Your email is valid")
#     else:
#         print("Your email is not valid")

