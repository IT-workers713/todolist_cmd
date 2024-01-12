def convert():
    liters = int(input("enter leters"))
    res = liters/1000
    message = f"{liters} liters == {res} cubic meter"
    return message


print(convert())


