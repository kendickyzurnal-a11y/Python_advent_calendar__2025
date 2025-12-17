from random import randint

pocet = int(input("Koľko má stromček svetielok? "))

svieti = 0

svetlo = 0

for i in range(pocet):
    svetlo = randint(0,1)
    if svetlo == 1:
        svieti += 1
    pass

print("Svieti", svieti, "svetielok 🎄")
