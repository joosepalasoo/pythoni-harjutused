#joosep alasoo
#tkinter yl02
#06.02.2024
from tkinter import *

#akna seaded
aken=Tk()
aken.title("kalkulaator")
aken.geometry("200x200")

#tekst
Text=Label(aken, text="siia kunagi vastus!", font="tahoma 12").pack()

#nupud
nupp1=Button(aken, text="1")
nupp1.grid(row=0, column=1)


aken.mainloop()