## 🎄🐍 **Python advent – DEŇ 6** 🐍🎄

**Téma: Čas (`time`) a oneskorenie**

Dnes sa naučíš **pracovať s časom** – čakať, počítať sekundy a robiť malé efekty ⏳🎄  
To sa hodí do hier, animácií aj programov so zvukom.

----------

## ⏰ Modul `time`

Najprv import:

`import time` 

----------

## 💤 `time.sleep()`

Program sa **na chvíľu zastaví**.

`import time print("Elf premýšľa...")
time.sleep(2) print("Hotovo 🎁")` 

➡️ číslo je **v sekundách**

----------

## ⏱️ Aktuálny čas

`import time

teraz = time.time() print(teraz)` 

🔹 vráti počet sekúnd od 1.1.1970  
(väčšinou ho používame na meranie času)

----------

## ⌛ Meranie trvania

`import time

start = time.time()

time.sleep(1.5)

koniec = time.time() print("Trvalo to", round(koniec - start, 2), "sekúnd")` 

----------

## 🎄 Príklad – Vianočné odpočítavanie

`import time for i in  range(5, 0, -1): print(i)
    time.sleep(1) print("🎄 Veselé Vianoce!")` 

----------

## 🎁 ÚLOHA – Odpočítavanie do darčeka

Napíš program, ktorý:

1.  spýta sa používateľa, **koľko sekúnd** má čakať
    
2.  odpočítava každú sekundu
    
3.  na konci vypíše vianočnú správu
    

### Pomocná kostra

`import time

sekundy = int(input("O koľko sekúnd otvoríme darček? ")) for i in  range(sekundy, 0, -1): # doplň výpis time.sleep(1) print("🎁 Darček otvorený!")` 

----------

## ⭐ Bonus úloha

-   použi **funkciu** na odpočítavanie
    
-   pridaj **bodky** počas čakania (`...`)
    
-   skombinuj s `randint` (náhodná dĺžka čakania)
    

----------

## ⚠️ Dôležité upozornenie

-   `sleep()` **zastaví celý program**
    
-   v GUI (tkinter) sa používa **inak** (to si ukážeme zajtra)


______

[INSTRUCTIONS FILE](https://kendickyzurnal-a11y.github.io/Python_advent_calendar__2025/day_6/day06.py)

[RIGHT ANSWER](https://kendickyzurnal-a11y.github.io/Python_advent_calendar__2025/day_6/day06_Odpo%C4%8D%C3%ADtavanie%20do%20dar%C4%8Deka_simple.py)

[RIGHT ANSWER (with bonus)](https://kendickyzurnal-a11y.github.io/Python_advent_calendar__2025/day_6/day06_Odpo%C4%8D%C3%ADtavanie%20do%20dar%C4%8Deka_bonus.py)
