from tkinter import *
from tkinter import ttk
root = Tk()
ent1 = ttk.Entry(root , width=50)
ent1.pack()
bu1 = ttk.Button(root, text="get text")
bu1.pack()

def buClick():
    print(ent1.get())
    ent1.delete(0,END)

bu1.config(command=buClick)

root.mainloop()

