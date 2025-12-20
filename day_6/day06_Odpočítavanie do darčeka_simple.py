import time

sekundy = int(input("O koľko sekúnd otvoríme darček? "))

for i in range(sekundy, 0, -1):
    print ("Čakaj na darček " + str(i) + " sekúnd!" )
    time.sleep(1)

print("🎁 Darček otvorený!")
