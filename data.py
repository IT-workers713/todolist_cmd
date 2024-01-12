def user(user_input):
    item  = user_input.split(',')
    return len (item)
name = input("enter your name ")
nr = user(name)
print(nr)