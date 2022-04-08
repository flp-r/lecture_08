import json
import numpy as np
names = ["Pablo Escobar", "Joaqim Guzmán", "Ismael Garcia"]
production = [(138, 164, 151), (125, 113, 113), (52, 50, 63)]
most_wanted = dict(zip(names, production))

origin = {
"Mexico": {"Manuel Noriega", "Pablo Escobar", "Joaqim Guzmán", "Ismael Garcia"},
"Columbia": {"Rick Ross", "William Jardine"},}

def main():
    with open("new_criminals.json", "r", encoding="utf-8") as file:
        new_criminals = json.load(file)
        # print(new_criminals)

    return new_criminals

# print(main())

def criminals(most_wanted):
    new_criminals = main()
    for key, value in new_criminals.items():
        most_wanted[key] = tuple(value)
    return most_wanted

print(criminals(most_wanted))

def get_production(state, origin, most_wanted):
    cislo = []
    for key, value in origin.items():
        if key == state:
            for man in value:
                m = most_wanted[man]
                m = list(m)
                cislo.append(m)

    cislo = np.array(cislo)
    suma = np.sum(cislo)
    return suma

print(get_production("Columbia", origin, most_wanted))



















