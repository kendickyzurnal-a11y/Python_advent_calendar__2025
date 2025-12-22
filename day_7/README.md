## 🎄🐍 **Python advent – DEŇ 7** 🐍🎄

**Téma: Kreslenie (`turtle`), zvuk a udalosti (myš + klávesnica)**

Dnes je to **zábavný deň** 😄  
Uvidíš, ako Python **reaguje na teba** – na stlačenie klávesu, klik myšou a ešte si niečo nakreslí.

----------

## 🐢 Kreslenie s `turtle`

`turtle` kreslí pomocou „korytnačky“.

### Základ

`import turtle`

`t = turtle.Turtle()`
`t.forward(100)`
`t.left(90)`
`t.forward(100)`

`turtle.done()` 

----------

## 🎄 Príklad – Vianočný stromček (jednoduchý)

`import turtle`

`t = turtle.Turtle()`
`t.speed(0) for i in  range(3):`
  `  t.forward(100)`
   ` t.left(120)`

`turtle.done()` 

----------

## 🖱️ UDALOSTI – myš

Turtle vie reagovať na **klik myšou**.

`import turtle`

`t = turtle.Turtle() def  klik(x, y):`
`    t.goto(x, y)`
`    t.dot(10, "red")`

`turtle.onscreenclick(klik)`
`turtle.done()` 

➡️ po kliknutí sa nakreslí bod

----------

## ⌨️ UDALOSTI – klávesnica

Najprv povieme, že **počúvame klávesy**:

`turtle.listen()` 

Potom priradíme funkcie:

`import turtle`

`t = turtle.Turtle() def  hore():`
 `   t.forward(20) def  vlavo():`
`    t.left(15) def  vpravo():`
 `   t.right(15)`

`turtle.listen()`
`turtle.onkey(hore, "Up")`
`turtle.onkey(vlavo, "Left")`
`turtle.onkey(vpravo, "Right")`

`turtle.done()` 

➡️ ovládaš korytnačku šípkami 🎮

----------

## 🔊 Zvuk (jednoducho)

Najjednoduchší spôsob (na Windows):

`import winsound`
`.Beep(800, 200)` 

⚠️ funguje len na **Windows**

Alternatíva (krížovo):

`print("\a")` 

----------

## 🎁 HLAVNÁ ÚLOHA – Vianočný ovládaný stromček

Uprav alebo doplň tento kód tak, aby:

1.  šípkami **hýbal korytnačku**
    
2.  klik myšou nakreslil **ozdobu**
    
3.  stlačenie klávesy `"space"` zahralo zvuk alebo vypísalo „cink“ 🔔
    

### Polopripravený kód

`import turtle`

`t = turtle.Turtle()`
`t.speed(0) def  hore():`
`    t.forward(20) def  dolu():`
`    t.backward(20) def  vlavo():`
`    t.left(15) def  vpravo():`
`    t.right(15) def  ozdoba(x, y):`
 `   t.goto(x, y)`
 `   t.dot(15, "red")`

`turtle.listen()`
`turtle.onkey(hore, "Up")`
`turtle.onkey(dolu, "Down")`
`turtle.onkey(vlavo, "Left")`
`turtle.onkey(vpravo, "Right")`
`turtle.onscreenclick(ozdoba)`
`turtle.done()` 

----------

## ⭐ Bonus

-   zmeň farby ozdôb náhodne (`randint`)
    
-   pridaj viac zvukov
    
-   obmedz pohyb len na obrazovku
    

----------

## ⚠️ Dôležité pravidlo (veľmi dôležité!)

❌ **NEPOUŽÍVAJ `time.sleep()` v turtle udalostiach**  
✔️ turtle pracuje **udalosťami**, nie čakaním

----------

Zajtra nás čaká 🎁 **DEŇ 8 – MINI PROJEKT**  
Spojíme **náhodu, funkcie, čas, udalosti aj kreslenie** 🎄👨‍💻🐍
____
[INSTRUCTIONS FILE](https://kendickyzurnal-a11y.github.io/Python_advent_calendar__2025/day_7/day07.py)


[RIGHT ANSWER](https://kendickyzurnal-a11y.github.io/Python_advent_calendar__2025/day_7/day07_Viano%C4%8Dn%C3%BD%20ovl%C3%A1dan%C3%BD%20strom%C4%8Dek_simple.py)


[RIGHT ANSWER (	with bonus )](https://kendickyzurnal-a11y.github.io/Python_advent_calendar__2025/day_7/day07_Viano%C4%8Dn%C3%BD%20ovl%C3%A1dan%C3%BD%20strom%C4%8Dek_bonus.py)


