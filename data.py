def water_state(tempature):
    x=0
    y=100
    if tempature <=x:
        return "SOLID"
    elif x<tempature<y:
        return "liquid"
    else:
        return "gaz"
temperatures = float(input("entrer temperature of water"))

state = water_state(temperatures)
print(state)

