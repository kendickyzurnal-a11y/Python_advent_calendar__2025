def vyrob_darceky(meno, pocet):
    emotikon = pocet*"🎁"
    return ("Elf vyrobil " + str(pocet) + " darčekov pre " + meno + ". " + emotikon )
    pass

print(vyrob_darceky("Anka", 3))
