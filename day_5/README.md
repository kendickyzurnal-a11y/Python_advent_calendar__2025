## 🎄🐍 **Python advent – DEŇ 5** 🐍🎄

**Téma: Funkcie (upevnenie a poriadok v kóde)**

Funkcie už **poznáš**, dnes si ich hlavne **utriedime v hlave** a použijeme ich prakticky.

----------

## 🔧 Prečo vlastne funkcie?

Funkcia je:

-   **kus kódu s menom**
    
-   ktorý môžeš **použiť viackrát**
    
-   a robí **jednu konkrétnu vec**
    

👉 podobne ako „elf, ktorý má jednu úlohu“ 🎅

----------

## 🧱 Základná štruktúra

`def  pozdrav(): print("Veselé Vianoce 🎄")

pozdrav()` 

----------

## 📥 Parametre

Funkcia môže dostať **vstupné hodnoty**:

`def  pozdrav(meno): print(f"Ahoj {meno}, veselé Vianoce 🎄")

pozdrav("Janko")` 

----------

## 📤 Návratová hodnota (`return`)

Funkcia môže **niečo vypočítať a vrátiť**:

`def  darcek(skutky): if skutky == 0: return  "uhlie"  elif skutky < 5: return  "malý darček"  else: return  "veľký darček"` 

Použitie:

`vysledok = darcek(3) print(vysledok)` 

----------

## ⚠️ Časté chyby

❌ zabudnutý `return`  
❌ `print` namiesto `return`  
❌ funkcia robí „všetko možné“ naraz

----------

## 🎄 Príklad – Funkcia + slovník

`deti = { "Janko": 5, "Anka": 2, "Marek": 0 } def  vyhodnot_dieta(skutky): if skutky == 0: return  "uhlie"  elif skutky < 5: return  "malý darček"  else: return  "veľký darček"  for meno, skutky in deti.items(): print(meno, "dostane", vyhodnot_dieta(skutky))` 

----------

## 🎁 ÚLOHA – Elfská továreň

Napíš **funkciu**, ktorá:

1.  má parameter `meno`
    
2.  má parameter `pocet_darcekov`
    
3.  vráti **textovú správu**
    

Príklad výstupu:

`Elf vyrobil 3 darčeky pre Anka 🎁🎁🎁` 

### Pomocná kostra

`def  vyrob_darceky(meno, pocet): # sem doplň kód  pass  print(vyrob_darceky("Anka", 3))` 

💡 Tip: použi `f-string` a násobenie reťazcov `"🎁" * pocet`

----------

## ⭐ Bonus úloha

-   funkcia nech **vracia reťazec**
    
-   `print()` použij až **mimo funkcie**
    

----------

[INSTUCTIONS FILE](https://kendickyzurnal-a11y.github.io/Python_advent_calendar__2025/day_5/day05.py)


[RIGHT ANSWER](https://kendickyzurnal-a11y.github.io/Python_advent_calendar__2025/day_5/day05_Elfsk%C3%A1%20tov%C3%A1re%C5%88_simple.py)

[RIGHT ANSWER (with bonus)](https://kendickyzurnal-a11y.github.io/Python_advent_calendar__2025/day_5/day05_Elfsk%C3%A1%20tov%C3%A1re%C5%88_bonus.py)
