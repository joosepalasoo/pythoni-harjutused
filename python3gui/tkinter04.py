#joosep alasoo
#tkinter yl04
#16.02.2024
from tkinter import *
from PIL import Image, ImageTk

#akna seaded
aken = Tk()
aken.title('Joonistamine')


#lõuendi loomine
louend = Canvas(aken, width=1000, height=1000)
louend.pack()

#kujundite loomine
louend.create_rectangle(0, 0, 500, 400, fill="red")
louend.create_rectangle(120, 0, 170, 400, fill="white")
louend.create_rectangle(500, 180, 0, 130, fill="white")


#pildi lisamine
minu_pilt = PhotoImage(file='pilt.png')
louend.create_image(600, 0, anchor=NW, image=minu_pilt)

aken.mainloop()