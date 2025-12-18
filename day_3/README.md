## 🎄🐍 **Python advent – DEŇ 3** 🐍🎄

**Téma: Zoznamy (`list`) a n-tice (`tuple`)**

Dnes budeme pracovať s **viac hodnotami naraz** – presne ako s vianočnými darčekmi 🎁🎁🎁

----------

## 📦 Zoznam (`list`)

-   **meniteľný** (môžeš ho upravovať)
    
-   používa sa najčastejšie
    

`darceky = ["autíčko", "bábika", "lego", "kniha"] print(darceky)` 

### Prístup k prvku

`print(darceky[0]) # prvý darček` 

### Prechod zoznamom

`for darcek in darceky: print(darcek)` 

----------

## 🔒 N-tica (`tuple`)

-   **nemeniteľná** (nedá sa meniť)
    
-   používa sa, keď sa hodnoty **nemajú zmeniť**
    

`dni = ("Pondelok", "Utorok", "Streda") print(dni[1])` 

❌ toto by nefungovalo:

`dni[0] = "Sobota"` 

----------

## 🤔 Kedy čo použiť?

-   **zoznam** → keď chceš pridávať, meniť, mazať
    
-   **n-tica** → keď má byť hodnota „pevná“
    

----------

## 🎲 Príklad – Náhodný darček

`from random import randint

darceky = ["ponožky", "čokoláda", "kniha", "lego", "hra"]

nahodny = randint(0, len(darceky) - 1) print("Dostal si:", darceky[nahodny])` 

----------

## 🎁 ÚLOHA – Vianočný zoznam darčekov

1.  vytvor zoznam **aspoň 5 darčekov**
    
2.  pomocou `for` cyklu ich vypíš s poradovým číslom
    
3.  náhodne vyber **jeden darček**
    
4.  vypíš správu pre používateľa
    

### Pomocná kostra

`from random import randint

darceky = [ # doplň darčeky ] for i in  range(len(darceky)): # vypíš poradové číslo a názov darčeka  pass nahodny = randint(0, len(darceky) - 1) print("🎁 Dnes dostávaš:", darceky[nahodny])` 

----------

## ⭐ Bonus úloha – N-tica

-   vytvor n-ticu s názvami **vianočných dní**
    
-   vypíš ich pomocou cyklu
    

Príklad:

`dni = ("Štedrý deň", "1. sviatok vianočný", "2. sviatok vianočný")` 

----------

Ak chceš:

-   pošli mi riešenie
    
-   alebo napíš **„ukáž riešenie“**
    
-   alebo pokračuj zajtra:  
    👉 **Python advent – deň 4**
    

Ideš výborne, toto je presne správne tempo 👨‍💻🎄🐍
