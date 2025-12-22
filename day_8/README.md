# 🖼️ Tkinter – úplné, ale jednoduché vysvetlenie

`tkinter` je **knižnica na tvorbu okien (GUI)** – programy s tlačidlami, textom, vstupmi, myšou, klávesnicou.

👉 Všetko beží v **okne**, nie v konzole.

----------

## 1️⃣ Základ okna

Každý tkinter program má **jedno hlavné okno**.

`import tkinter as tk

root = tk.Tk()
root.title("Vianočný program")
root.mainloop()` 

-   `Tk()` → vytvorí okno
    
-   `title()` → názov okna
    
-   `mainloop()` → čaká na udalosti (kliknutia, klávesy)
    

⚠️ Bez `mainloop()` by sa okno hneď zavrelo.

----------

## 2️⃣ Text v okne – `Label`

Používa sa na **zobrazenie textu**.

`label = tk.Label(root, text="🎄 Veselé Vianoce!")
label.pack()` 

-   `text` → čo sa zobrazí
    
-   `pack()` → povie tkinteru: „zobraz to“
    

----------

## 3️⃣ Tlačidlo – `Button`

Tlačidlo **niečo vykoná po kliknutí**.

`def  klik(): print("Klikol si")

btn = tk.Button(root, text="Klikni", command=klik)
btn.pack()` 

👉 `command` = funkcia, ktorá sa spustí  
⚠️ **bez zátvoriek** (`klik`, nie `klik()`)

----------

## 4️⃣ Vstup od používateľa – `Entry`

Pole, kde používateľ **niečo napíše**.

`entry = tk.Entry(root)
entry.pack()

text = entry.get() # získa napísaný text` 

----------

## 5️⃣ Spájanie s Python logikou

Tkinter len:

-   zbiera vstup
    
-   zobrazuje výstup
    

**Rozhodovanie, náhoda, cykly** sú normálny Python.

----------

## 🎄 Mini ukážka – všetko dokopy

`import tkinter as tk from random import randint def  darcek():
    meno = entry.get()
    darceky = ["lego", "kniha", "čokoláda"]
    vybrany = darceky[randint(0, len(darceky)-1)]
    label.config(text=f"🎁 {meno}, dostávaš {vybrany}")

root = tk.Tk()
root.title("Vianočný pomocník")

entry = tk.Entry(root)
entry.pack()

btn = tk.Button(root, text="Daj darček", command=darcek)
btn.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()` 

----------

# 🎁 DEŇ 8 – Mini projekt (tkinter verzia)

## 🎄 Zadanie

Vytvor **vianočný GUI program**, ktorý:

1.  má **okno**
    
2.  má **Entry** na meno
    
3.  má **Entry** na počet dobrých skutkov
    
4.  má **Button**
    
5.  po kliknutí:
    
    -   rozhodne darček (`if`)
        
    -   použije `randint`
        
    -   vypíše výsledok do `Label`
        

----------

## 🛠️ Pripravená kostra (doplň logiku)

`import tkinter as tk from random import randint def  rozhodni():
    meno = meno_entry.get()
    skutky = int(skutky_entry.get())

    darceky = ["lego", "kniha", "čokoláda", "hra"] # TODO: doplň rozhodovanie # if ...  # label.config(text="...") root = tk.Tk()
root.title("🎄 Vianočný pomocník")

tk.Label(root, text="Meno:").pack()
meno_entry = tk.Entry(root)
meno_entry.pack()

tk.Label(root, text="Počet dobrých skutkov:").pack()
skutky_entry = tk.Entry(root)
skutky_entry.pack()

btn = tk.Button(root, text="Rozhodni darček 🎁", command=rozhodni)
btn.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()` 

----------

## ⭐ Bonus (nepovinné)

-   pridaj **kontrolu chyby** (ak niekto zadá text namiesto čísla)
    
-   zmeň **farby / font**
    
-   pridaj **tlačidlo „Znova“**
    
-   pridaj **odpočítavanie cez `after()`**
    

----------

🎉 **Ak toto dokončíš, zvládol si:**

-   tkinter
    
-   udalosti (klik)
    
-   vstup / výstup
    
-   podmienky
    
-   náhodu
    
-   mini GUI projekt
    

Keď budeš hotový:

-   pošli kód
    
-   alebo chceš **rozšírenie** (klávesy, myš, hra)
    

**Výborne si to dotiahol až do konca 👨‍💻🎄🐍**

___________________


[INSTRUCTIONS FILE](https://kendickyzurnal-a11y.github.io/Python_advent_calendar__2025/day_8/day08_a.py)


[RIGTH ANSWER](https://kendickyzurnal-a11y.github.io/Python_advent_calendar__2025/day_8day08_a_Mini%20tkinter%20projekt.py)
