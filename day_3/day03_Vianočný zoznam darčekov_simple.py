from random import randint

darceky = [ "Ponožky", "Hrnček", "Kniha", "Voňavka", "Plyšák", "Poukážka"]

for i in range(len(darceky)):
    print (darceky[i])
    pass

nahodny = randint(0, len(darceky) - 1)
print("🎁 Dnes dostávaš:", darceky[nahodny])
