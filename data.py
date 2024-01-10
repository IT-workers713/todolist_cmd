while True:
    with open('coin.txt','r') as file:
        sides=file.readlines()

    side = input("Throw the coin and enter head or tail here: ?") + "\n"
    sides.append(side)

    with open('coin.txt','w') as file:
        file.writelines(sides)
    nbr = sides.count('heaad')
    pr = nbr/len(sides)*100
    print(f"percentages {pr}%")