def water_state(tempature):
    if tempature <=0:
        return "SOLID"
    elif 0<tempature<100:
        return "liquid"
    else:
        return "gaz"
temperatures = float(input("entrer temperature of water"))

state = water_state(temperatures)
print(state)

