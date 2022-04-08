import json
names = ["Pablo Escobar", "Joaqim Guzmán", "Ismael Garcia"]
production = [(138, 164, 151), (125, 113, 113), (52, 50, 63)]
most_wanted = dict(zip(names, production))

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














