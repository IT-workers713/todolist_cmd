try:
    nombre = int(input("enter une valeur totale : \n"))
    valeur = int(input("enter une valeur : \n"))

    res  = valeur * 100/nombre
    print("that is :",res)
except ValueError:
    print("il faut que vous entrerez un nombre pas une chaine !!")
except ZeroDivisionError:
    print("en peut pas deviser un 0 sur un nombre")