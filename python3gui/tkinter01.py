#joosep alasoo
#tkinter yl01
#06.02.2024
from tkinter import *

aken = Tk()
aken.title("joosep alasoo")
aken.resizable(0, 0)
aken.configure(background="black")
tekst = Label(aken, pady="20", padx="20", fg="red", bg="black", font="tahoma 16 bold italic", text="Nimi: joosep alasoo\nRühm: IT23\n2024").pack()

aken.mainloop()