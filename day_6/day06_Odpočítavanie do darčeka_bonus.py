from random import randint
import time

sekundy = randint (3, 15)


def cakaj_na_darcek(cas):
    print ("Čakaj na darček ", end= "")
    for i in range(cas, 0, -1):
        print (".", end= "", flush=True)
        time.sleep(1)
    print ("🎁 Darček otvorený!")
    
cakaj_na_darcek(sekundy)
