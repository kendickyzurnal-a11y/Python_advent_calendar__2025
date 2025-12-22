import tkinter as tk
from random import randint

def rozhodni():
    meno = meno_entry.get()
    skutky = int(skutky_entry.get())

    darceky = ["lego", "kniha", "čokoláda", "hra"]

    # TODO: doplň rozhodovanie
    # if ...
    # label.config(text="...")

root = tk.Tk()
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

root.mainloop()
