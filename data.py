password = input("entrez votre mot de passe : \n")
#t checks if the password length is greater than 7 and returns "Great password there!".

if len(password) > 7:
    print("Great password there!")
#If the password has 7 or fewer characters, the program returns, "Your password is weak".
elif len(password)<7:
    print("Your password is weak")
elif len(password)==7:
    print("password to weak you need to enter another password")
