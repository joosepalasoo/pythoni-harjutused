#joosep alasoo
#tkinter yl04
#16.02.2024
from tkinter import *

#akna seaded
aken = Tk()
aken.title('Joonistamine')


#lõuendi loomine
louend = Canvas(aken, width=500, height=500)
louend.pack()

#kujundite loomine
louend.create_rectangle(0, 0, 500, 400, fill="red")
louend.create_rectangle(120, 0, 170, 400, fill="white")
louend.create_rectangle(500, 180, 0, 130, fill="white")


aken.mainloop()