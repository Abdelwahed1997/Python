def user_pass_check():
    user = [{"name":"abdelwahed","pass":"159357"},{"name":"ali","pass":"7877"}]
    user_input=input("enter ur name:  ")
    for i in user:
        if i["name"] ==user_input:
            userPass=input("enter ur pass:  ")
            if i["pass"] ==userPass:
                print("Your password is correct")
                break
            else:
                print("Your password is incorrect")
            break
        
        else:
            continue
    else:
        print("not found")

user_pass_check()