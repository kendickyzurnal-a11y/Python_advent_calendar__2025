import tkinter as tk
from random import randint

def rozhodni():
    meno = meno_entry.get()
    skutky = int(skutky_entry.get())

    male_darceky = ["hračka", "voňavé mydlo", "rodinná fotka", "jedlo"]
    velke_darceky = ["lego", "kniha", "čokoláda", "hra"]

    if skutky == 0:
        vypis = meno + " dostáva uhlie."
        label = tk.Label(root, text= vypis)
        label.pack()
    elif skutky > 0 and skutky < 5:
        vypis = meno + " dostáva " + male_darceky [randint (0, 3)] + "."
        label = tk.Label(root, text= vypis)
        label.pack()
    else:
        vypis = meno + " dostáva " + velke_darceky [randint (0, 3)] + "."
        label = tk.Label(root, text= vypis)
        label.pack()


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
