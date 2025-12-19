## 🎄🐍 **Python advent – DEŇ 4** 🐍🎄

**Téma: Slovníky (`dict`)**

Dnes si osvojíš jednu z **najdôležitejších dátových štruktúr v Pythone**.  
Slovník funguje ako **mapa: kľúč → hodnota** 🗺️🎁

----------

## 📘 Základ slovníka

`darceky = { "Janko": "lego", "Anka": "kniha", "Marek": "autíčko" }` 

-   **kľúč**: meno
    
-   **hodnota**: darček
    

----------

## 🔍 Prístup k hodnote

`print(darceky["Janko"])` 

----------

## ➕ Pridanie / zmena

`darceky["Eva"] = "plyšák" darceky["Janko"] = "hra"` 

----------

## 🔁 Prechod slovníkom

### Kľúče

`for meno in darceky: print(meno)` 

### Kľúč + hodnota

`for meno, darcek in darceky.items(): print(meno, "dostane", darcek)` 

----------

## 🎲 Príklad – Náhodný výber osoby

`from random import choice

mena = list(darceky.keys())
vybrane = choice(mena) print(vybrane, "dostane", darceky[vybrane])` 

----------

## 🎁 ÚLOHA – Mikulášov zoznam

Napíš program, ktorý:

1.  vytvorí slovník **meno → počet dobrých skutkov**
    
2.  prejde celý slovník
    
3.  podľa počtu skutkov priradí darček:
    
    -   0 → uhlie
        
    -   1–4 → malý darček
        
    -   5+ → veľký darček
        
4.  vypíše výsledok
    

### Pomocná kostra

`deti = { "Janko": 5, "Anka": 2, "Marek": 0, # doplň ďalšie } for meno, skutky in deti.items(): # doplň podmienky  pass` 

----------

## ⭐ Bonus úloha

-   pridaj **nové dieťa** zo vstupu (`input`)
    
-   ulož ho do slovníka
    
-   znovu vypíš celý zoznam

----------

[INSTRUCTIONS FILE](https://kendickyzurnal-a11y.github.io/Python_advent_calendar__2025/day_4/day04.py)
