# 1️⃣ UDALOSTI v tkinteri (klávesnica, myš)

Tkinter funguje **udalostne**:

> „Keď sa NIEČO stane → spustí sa funkcia“

----------

## ⌨️ Klávesnica

`def  klaves(event): print("Stlačený kláves:", event.keysym)

root.bind("<Key>", klaves)` 

-   `event.keysym` → názov klávesy (`a`, `Left`, `Return`, …)
    
-   okno musí byť **aktívne**
    

----------

## 🖱️ Myš

`def  klik(event): print("Klik na:", event.x, event.y)

canvas.bind("<Button-1>", klik)` 

-   `event.x`, `event.y` → súradnice kliknutia
    

----------

# 2️⃣ KRESLENIE – `Canvas`

`Canvas` je **kresliaca plocha**.

`canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()` 

----------

## 🎄 Základné tvary

`canvas.create_oval(150, 50, 250, 150, fill="green") # guľa canvas.create_rectangle(180, 150, 220, 220, fill="brown") # kmeň canvas.create_text(200, 20, text="🎄", font=("Arial", 20))` 

👉 Všetko je dané súradnicami.

----------

# 3️⃣ ČAS – `after()` (správny tkinter spôsob)

❌ **NEPOUŽÍVAJ `time.sleep()` v tkinteri**  
(okno by zamrzlo)

✅ Používaj:

`def  sprava():
    label.config(text="🎄 Veselé Vianoce!")

root.after(2000, sprava) # po 2 sekundách` 

----------

## ⏳ Opakovanie (animácia)

`def  blikaj():
    canvas.itemconfig(stromcek, fill="green")
    root.after(500, lambda: canvas.itemconfig(stromcek, fill="darkgreen"))
    root.after(1000, blikaj)` 

----------
# 1️⃣ Každý tvar má ID

Keď niečo nakreslíš, tkinter ti vráti **číslo objektu**.

`strom = canvas.create_polygon(..., fill="green")` 

`strom` je **ID stromčeka**.

----------

# 2️⃣ Súradnice objektu

Každý objekt má **hranice (bounding box)**:

`canvas.bbox(strom)` 

Vracia:

`(x1, y1, x2, y2)` 

➡️ ľavý horný roh a pravý dolný roh

----------

# 3️⃣ Zistenie, či bod je „na objekte“

Keď klikneš myšou, máš:

`event.x, event.y` 

A teraz logika:

`x1, y1, x2, y2 = canvas.bbox(strom) if x1 <= event.x <= x2 and y1 <= event.y <= y2: print("Klikol si na stromček 🎄")` 

🔥 **Toto je presne „dotýka sa farby“**  
(len technicky správne: dotýka sa objektu)

----------

# 4️⃣ Praktický mini príklad (klik na stromček)

`def  klik(event):
    x1, y1, x2, y2 = canvas.bbox(strom) if x1 <= event.x <= x2 and y1 <= event.y <= y2:
        canvas.create_text(200, 30, text="🎄 Stromček!", font=("Arial", 16))` 

`canvas.bind("<Button-1>", klik)` 

----------

# 5️⃣ Dotyk dvoch objektov (kolízia)

Ak máš napr.:

-   ozdobu
    
-   stromček
    

`o1 = canvas.bbox(ozdoba)
o2 = canvas.bbox(strom) def  dotyk(a, b): return  not (
        a[2] < b[0] or a[0] > b[2] or a[3] < b[1] or a[1] > b[3]
    ) if dotyk(o1, o2): print("Ozdoba je na stromčeku 🎄")` 

----------

# 6️⃣ Bonus – `find_overlapping` (ešte lepšie)

Tkinter má **hotovú funkciu**:

`objekty = canvas.find_overlapping(event.x, event.y, event.x, event.y) if strom in objekty: print("Dotkol si sa stromčeka 🎄")` 

👉 Toto je **najčistejšie riešenie**  
👉 Odporúčam ho pre teba 👌

----------

# 🎄 Ako to použiť v tvojom projekte

Môžeš spraviť:

-   ozdoby sa **pridajú iba ak klikneš na stromček**
    
-   mimo stromčeka sa klik ignoruje
    
-   pri dotyku sa zmení farba
    
-   zobrazí sa text / zvuk
---------
---------

## ZVUK

# 🔊 1️⃣ Najjednoduchšie – `winsound` (Windows)

Ak máš **Windows**, toto je najľahšia cesta.

`import winsound

winsound.Beep(800, 300) # frekvencia, dĺžka v ms` 

Alebo zvuk zo súboru:

`winsound.PlaySound("zvuk.wav", winsound.SND_FILENAME)` 

⚠️ Funguje **len na Windows**.

----------

# 🔊 2️⃣ Univerzálne – `pygame.mixer` ⭐ (ODPORÚČAM)

Funguje na **Windows / Linux / macOS**  
Veľmi jednoduché na zvuky.

### Inštalácia (raz):

`pip install pygame` 

### Použitie:

`import pygame

pygame.mixer.init()
pygame.mixer.Sound("zvuk.wav").play()` 

👉 ideálne pre:

-   kliknutia
    
-   efekty
    
-   hry
    

----------

# 🔊 3️⃣ Jednoduchý systémový zvuk – `bell`

Tkinter vie aspoň:

`root.bell()` 

🔔 len „pípnutie“, žiadny súbor

----------

# 🎄 Ako to spojiť s tkinter udalosťou

Napríklad **pri kliknutí na stromček**:

`def  klik(event):
    pygame.mixer.Sound("ding.wav").play()` 

Alebo:

`def  klik(event):
    root.bell()` 

----------

# ⚠️ Dôležité pravidlá

-   **NEPOUŽÍVAJ `time.sleep()` so zvukom v tkinteri**
    
-   zvuk **nesmie blokovať okno**
    
-   `pygame.mixer` je na to najlepší
    

----------

# 🎁 Príklad – zvuk pri ozdobe 🎄

    `import tkinter as tk import pygame
    
    pygame.mixer.init()
    zvuk = pygame.mixer.Sound("ding.wav") def  pridaj(event):
        zvuk.play()
        canvas.create_oval(event.x, event.y, event.x+10, event.y+10, fill="red")`

 ------------
 # 🔊 1️⃣ `playsound` – úplne najjednoduchšie

Veľmi populárna knižnica.

### Inštalácia:

`pip install playsound` 

### Použitie:

`from playsound import playsound

playsound("zvuk.mp3")` 

✅ funguje na Windows / macOS / Linux  
❌ **blokuje program** (okno na chvíľu zamrzne)

👉 **NEODPORÚČAM pre tkinter hry**, ale OK na:

-   krátke zvuky
    
-   testovanie
    

----------

# 🔊 2️⃣ `simpleaudio` ⭐ (veľmi dobrá alternatíva)

Ľahká, rýchla, **neblokuje GUI**.

### Inštalácia:

`pip install simpleaudio` 

### Použitie:

`import simpleaudio as sa

wave = sa.WaveObject.from_wave_file("zvuk.wav")
wave.play()` 

✅ multiplatformová  
✅ neblokuje tkinter  
❌ len `.wav`

👉 **výborná voľba pre teba**, ak nechceš pygame

----------

# 🔊 3️⃣ `sounddevice` (pokročilejšie)

Používa sa aj na:

-   nahrávanie
    
-   generovanie zvuku
    
-   signály
    

`pip install sounddevice soundfile` 

`import sounddevice as sd import soundfile as sf

data, fs = sf.read("zvuk.wav")
sd.play(data, fs)` 

✅ profesionálne  
❌ zložitejšie  
👉 skôr pre audio projekty

----------

# 🔊 4️⃣ `os` + systémový prehrávač (núdzové riešenie)

`import os
os.system("start zvuk.wav") # Windows` 

❌ nepresné  
❌ závislé od systému  
❌ nekontrolovateľné

----------

# 🏆 POROVNANIE (rýchly prehľad)

|Knižnica|  Multiplatform| Neblokuje| Vhodné pre `tkinter`|
|--|--|--|--|
| `winsound` | ❌ | ❌|⚠️ len Windows  |
| `playsound` | ✅ | ❌|❌  |
| `simpleaudio` | ✅ | ✅|⭐⭐⭐⭐  |
| `pygame.mixer` | ✅ | ✅|⭐⭐⭐⭐⭐  |
| `sounddevice` | ✅ | ✅|⭐⭐⭐  |


# 🎄 Čo odporúčam pre tvoj projekt

👉 **`pygame.mixer` alebo `simpleaudio`**

 1.   chceš **jednoduchosť** → `simpleaudio`
    
 2.   chceš **viac zvukov, hry** → `pygame`
-----------
## INŠTALÁCIA `SOUNDDEVICE`...
 1. Otvor príkazový riadok a napíš:
   `pip install sounddevice soundfile`
alebo
    `py -m pip install soundfile sounddevice`
 
 2. Ak sa ti to podarilo nainštalovať, tak potom už len importuj do projektu: `import sounddevice as sd`
`import soundfile as sf`
 --------
 # 🔊 Ako v `sounddevice` prehrať vlastný zvuk

`sounddevice` **neprehráva súbory priamo**.  
Potrebujeme ešte **`soundfile`**, ktorý načíta `.wav`.

## 1️⃣ Skontroluj, že máš aj `soundfile`

`python -m pip install soundfile` 

Ak sa nainštaluje bez chyby → ideš ďalej 👍

----------

## 2️⃣ Priprav si zvuk

-   formát: **`.wav`**
    
-   krátky zvuk (klik, zvonček, píp)
    

Napríklad:

`klik.wav` 

v rovnakom priečinku ako `.py` súbor.

----------

## 3️⃣ Najjednoduchší kód (test)

`import sounddevice as sd import soundfile as sf

data, samplerate = sf.read("klik.wav")

sd.play(data, samplerate)
sd.wait() # počká, kým zvuk dohrá` 

▶️ Spusť program → mal by sa prehrať zvuk.

----------

# ⚠️ DÔLEŽITÉ PRE TKINTER

❌ `sd.wait()` **zastaví okno**  
✅ v GUI ho **nepoužívaj**

Správna verzia pre tkinter:

`sd.play(data, samplerate)` 

bez `wait()`.

----------

# 🎄 Použitie v tkinteri (klik, udalosť)

`import tkinter as tk import sounddevice as sd import soundfile as sf

root = tk.Tk()

data, fs = sf.read("klik.wav") def  klik(event=None):
    sd.play(data, fs)

btn = tk.Button(root, text="Klikni 🎄")
btn.pack()
btn.bind("<Button-1>", klik)

root.mainloop()` 

----------

# 🔹 Viac zvukov

`zvuky = { "klik": sf.read("klik.wav"), "chyba": sf.read("chyba.wav"),
} def  prehraj(nazov):
    data, fs = zvuky[nazov]
    sd.play(data, fs)` 

----------

# 🔹 Opakovanie zvuku (loop)

`sd.play(data, fs, loop=True)` 

Zastavenie:

`sd.stop()` 

----------

# 🔹 Generovanie vlastného zvuku (BONUS)

`import numpy as np

fs = 44100 t = np.linspace(0, 0.3, int(fs*0.3), False)
tone = 0.3 * np.sin(2 * np.pi * 880 * t)

sd.play(tone, fs)` 

----------

# 🧠 Prečo je `sounddevice` super

-   ✅ funguje na Py 3.14
    
-   ✅ neblokuje tkinter
    
-   ✅ vie prehrávať aj generovaný zvuk
    
-   ❌ potrebuje `.wav` alebo numpy pole


________
_______

# 🎁 TERAZ ÚLOHA – DEŇ 8 MINI PROJEKT 🎄

## 🎄 Názov:

**Vianočný stromček – interaktívny**

----------

## 🧩 Čo MUSÍ program obsahovať

✔ tkinter okno  
✔ `Canvas` (kreslenie)  
✔ **udalosti** (klik alebo klávesa)  
✔ **čas (`after`)**  
✔ náhodu (`randint`)

----------

## 🎄 Funkčnosť programu

1.  Po spustení sa zobrazí **stromček**
    
2.  Po **kliknutí myšou**:
    
    -   sa pridá **ozdoba na kliknuté miesto**
        
3.  Po stlačení klávesy **SPACE**:
    
    -   zobrazí sa vianočný text po oneskorení
        
4.  Stromček **bliká** (čas)
5. Pri kliknutí na tlačidlo pod obrazovkou sa pustí koleda
6. Pri kliknutí na druhé tlačidlo sa pridá darček
    

----------

## 🛠️ Pripravená kostra (dopĺňaš logiku)

`import tkinter as tk from random import randint

root = tk.Tk()
root.title("🎄 Vianočný stromček")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack() # stromček strom = canvas.create_polygon( 200, 50, 100, 300, 300, 300,
    fill="green" ) # blikajúci efekt  def  blikaj():
    canvas.itemconfig(strom, fill="green")
    root.after(500, lambda: canvas.itemconfig(strom, fill="darkgreen"))
    root.after(1000, blikaj) # klik myšou – pridaj ozdobu  def  pridaj_ozdobu(event):
    x = randint(120, 280)
    y = randint(80, 280)
    canvas.create_oval(x, y, x+10, y+10, fill="red") # klávesnica  def  klaves(event): if event.keysym == "space":
        root.after(1000, lambda: canvas.create_text( 200, 350, text="🎄 Veselé Vianoce!", font=("Arial", 16)
        ))

canvas.bind("<Button-1>", pridaj_ozdobu)
root.bind("<Key>", klaves)

blikaj()
root.mainloop()` 

----------

## ⭐ Bonus výzvy

-   rôzne farby ozdôb
    
-   pohyb ozdôb
    
-   počítadlo kliknutí
    
-   tlačidlo „Vymaž stromček“
    

----------

🎉 **Ak toto zvládneš**, už:

-   rozumieš **GUI**
    
-   chápeš **udalosti**
    
-   vieš kresliť
    
-   vieš pracovať s časom
    
-   a spojil si to do projektu


[INSTRUCTIONS FILE](https://kendickyzurnal-a11y.github.io/Python_advent_calendar__2025/project/day08_b.py)

[FINAL OUTPUT FILES (in `zip`)](https://kendickyzurnal-a11y.github.io/Python_advent_calendar__2025/project/project.zip)
