def calculate(year,current=2024):
    age = current-year
    return age
calcul = int(input("enter votre anné de naissance : "))
print(calculate(calcul,2024))
if calculate(calcul) > 120:
    print("vous etes chickour")