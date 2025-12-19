deti = {
    "Janko": 5,
    "Anka": 2,
    "Marek": 0,
    "Mišo": 3,
    "Juraj": 1,
    "Mária": 4,
    "Filip": 6,
    "Peter": 2,
    "Marcel": 8,
}

for meno, skutky in deti.items():
    print(meno, " urobil ", skutky, " dobrých skutkov. ")
    if skutky == 0:
        print (meno," dostáva uhlie." )
    elif skutky < 5 and skutky > 0:
        print (meno," dostáva malý darček." )
    else:
        print (meno, " dostáva veľký darček.")
    pass
