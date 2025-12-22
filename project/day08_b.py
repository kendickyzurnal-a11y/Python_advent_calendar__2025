import tkinter as tk
from random import randint

root = tk.Tk()
root.title("🎄 Vianočný stromček")

canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# stromček
strom = canvas.create_polygon(
    200, 50, 100, 300, 300, 300,
    fill="green"
)

# blikajúci efekt
def blikaj():
    canvas.itemconfig(strom, fill="green")
    root.after(500, lambda: canvas.itemconfig(strom, fill="darkgreen"))
    root.after(1000, blikaj)

# klik myšou – pridaj ozdobu
def pridaj_ozdobu(event):
    x = randint(120, 280)
    y = randint(80, 280)
    canvas.create_oval(x, y, x+10, y+10, fill="red")

# klávesnica
def klaves(event):
    if event.keysym == "space":
        root.after(1000, lambda: canvas.create_text(
            200, 350, text="🎄 Veselé Vianoce!", font=("Arial", 16)
        ))

canvas.bind("<Button-1>", pridaj_ozdobu)
root.bind("<Key>", klaves)

blikaj()
root.mainloop()
