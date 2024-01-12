password= input("enter new password \n")

def best_password():
    if len(password) < 8:
        print("password weak")
    elif len(password)==8:
        print("password weak")
    elif any(p.isupper() for p in password ) and len(password) > 8 and any(p.isdigit() for p in password):
        print("password strong")
    else:
        print("password weak")

best_password()


