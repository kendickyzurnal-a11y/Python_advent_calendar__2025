from random import randint

darceky = [ "Ponožky", "Hrnček", "Kniha", "Voňavka", "Plyšák", "Poukážka"]

for i in range(len(darceky)):
    print (darceky[i])
    pass

nahodny = randint(0, len(darceky) - 1)
print("🎁 Dnes dostávaš:", darceky[nahodny])
# BONUS
dni = ("Štedrý deň", "Prvý sviatok Vianočný", "Druhý sviatok Vianočný", "Nedeľa", "Pondelok", "Utorok", "Silvester", "Nový rok", "Piatok", "Sobota", "Nedeľa", "Pondelok", "Tri Krále")
print ("")
for a in range (len(dni)):
    print (dni[a])
