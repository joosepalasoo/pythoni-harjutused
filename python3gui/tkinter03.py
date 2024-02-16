#joosep alasoo
#tkinter yl03
#16.02.2024
from tkinter import *
from tkinter import ttk

#akna seaded
aken=Tk()
aken.title("käibemaksu kalkulaator")
aken.geometry("300x200")



#funktsioonid
def arvuta():
    hind=float(sisestus.get())
    km=var.get()/100
    arvutus=hind+hind*km
    print(arvutus)
    valjund1.config(text=str(km*hind)+"€")
    valjund2.config(text=hind)
#rida1
silt1 = Label(aken, text="hind käibemaksuta:")
silt1.grid(row=0,column=0)

sisestus = Entry(aken)
sisestus.grid(row=0,column=1)
#rida2-3
silt2 = Label(aken, text="käibemaksu määr:")
silt2.grid(row=1,column=0)

var = IntVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=9)
valikukast.grid(row=1, column=1)
valikukast = Radiobutton(aken,text="22%", variable=var, value=22)
valikukast.grid(row=2, column=1)

#rida4
joon=ttk.Separator(aken, orient='horizontal')
joon.grid(row=3, column=0, ipadx=100, columnspan=2)

#rida5
silt3 = Label(aken, text="käibemaks")
silt3.grid(row=4,column=0)

valjund1 = Label(aken, text="0.00€")
valjund1.grid(row=4,column=1)

#silt
silt4 = Label(aken, text="hind käibemaksuta:")
silt4.grid(row=5,column=0)

valjund2 = Label(aken, text="0.00€")
valjund2.grid(row=5,column=1)

#nupud
nupp1 = Button(aken, text="arvuta", width=10, command=arvuta)
nupp1.grid(row=6, columnspan=2)

aken.mainloop()