import time

sekundy = int(input("O koľko sekúnd otvoríme darček? "))

for i in range(sekundy, 0, -1):
    # doplň výpis
    time.sleep(1)

print("🎁 Darček otvorený!")
