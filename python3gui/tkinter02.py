#joosep alasoo
#tkinter yl02
#16.02.2024
from tkinter import *

#akna seaded
aken=Tk()
aken.title("kalkulaator")
aken.geometry("200x200")

#tekst
text=Label(aken, text="siia kunagi vastus!", font="tahoma 12")
text.grid(row=0, column=0, columnspan=4, padx=2, pady=2)
#nupud

nupp1 = Button(aken, text="7", font=("tahoma", 12) , width=4)
nupp1.grid(row=1, column=0, padx=2, pady=2)
nupp2 = Button(aken, text="8", font=("tahoma", 12) , width=4)
nupp2.grid(row=1, column=1, padx=2, pady=2)
nupp3 = Button(aken, text="9", font=("tahoma", 12) , width=4)
nupp3.grid(row=1, column=2, padx=2, pady=2)
nupp4 = Button(aken, text="/", font=("tahoma", 12) , width=4)
nupp4.grid(row=1, column=3, padx=2, pady=2)

nupp1 = Button(aken, text="4", font=("tahoma", 12) , width=4)
nupp1.grid(row=2, column=0, padx=2, pady=2)
nupp2 = Button(aken, text="5", font=("tahoma", 12) , width=4)
nupp2.grid(row=2, column=1, padx=2, pady=2)
nupp3 = Button(aken, text="6", font=("tahoma", 12) , width=4)
nupp3.grid(row=2, column=2, padx=2, pady=2)
nupp4 = Button(aken, text="*", font=("tahoma", 12) , width=4)
nupp4.grid(row=2, column=3, padx=2, pady=2)

nupp1 = Button(aken, text="1", font=("tahoma", 12) , width=4)
nupp1.grid(row=3, column=0, padx=2, pady=2)
nupp2 = Button(aken, text="2", font=("tahoma", 12) , width=4)
nupp2.grid(row=3, column=1, padx=2, pady=2)
nupp3 = Button(aken, text="3", font=("tahoma", 12) , width=4)
nupp3.grid(row=3, column=2, padx=2, pady=2)
nupp4 = Button(aken, text="-", font=("tahoma", 12) , width=4)
nupp4.grid(row=3, column=3, padx=2, pady=2)

nupp1 = Button(aken, text="0", font=("tahoma", 12) , width=4)
nupp1.grid(row=4, column=0, padx=2, pady=2)
nupp2 = Button(aken, text=",", font=("tahoma", 12) , width=4)
nupp2.grid(row=4, column=1, padx=2, pady=2)
nupp3 = Button(aken, text="=", font=("tahoma", 12) , width=4)
nupp3.grid(row=4, column=2, padx=2, pady=2)
nupp4 = Button(aken, text="+", font=("tahoma", 12) , width=4)
nupp4.grid(row=4, column=3, padx=2, pady=2)





aken.mainloop()