

## 🎄🐍 **Python advent – DEŇ 2** 🐍🎄

  
**Téma: Cykly + náhoda (`randint`)**

Dnes budeme **opakovať veci**, presne na to sú cykly ako stvorené 😉  
A pridáme aj **trochu vianočnej náhody** 🎲🎄

----------

## 🔁 Rýchle zopakovanie

### `for` cyklus

Používa sa, keď **vieme koľkokrát** sa má niečo opakovať.

`for i in  range(5): print("🎄")` 

➡️ vypíše stromček 5×

----------

### `while` cyklus

Používa sa, keď **nevieme dopredu**, koľkokrát sa to zopakuje (väčšinou opakuje stále).

`while  True: print("Ho ho ho!") break` 

----------

## 🎲 Náhoda – `randint`

Najprv import:

`from random import randint` 

Použitie:

`cislo = randint(1, 6) # náhodné číslo od 1 do 6  print(cislo)` 

----------

## 🎄 Príklad – Vianočné svetielka

Program náhodne rozhodne, či je svetielko zapnuté alebo vypnuté.

`from random import randint`
`for i in  range(10):`
    stav = randint(0, 1) 
    if stav == 1: print("💡 Svetielko svieti") else: print("⚫ Svetielko nesvieti")` 

----------

## 🎁 ÚLOHA – Rozsvieť stromček

Napíš program, ktorý:

1.  sa spýta, **koľko svetielok** má stromček
    
2.  pomocou `for` cyklu každému svetielku priradí:
    
    -   náhodne zapnuté alebo vypnuté
        
3.  vypíše výsledok
    
4.  **bonus**: spočíta, koľko ich svieti
    

### Pomocná kostra

`from random import randint

pocet = int(input("Koľko má stromček svetielok? "))

svieti = 0  for i in  range(pocet): # doplň kód  pass  print("Svieti", svieti, "svetielok 🎄")` 

💡 _Tip:_ keď svetielko svieti, zvýš `svieti` o 1.

----------

## ❄️ Bonus úloha (nepovinné)

-   vypíš aj **poradové číslo svetielka**
    
-   použi **spájanie reťazcov** alebo `f-string`
    

Príklad:

`print(f"Svetielko {i+1} svieti 💡")` 


