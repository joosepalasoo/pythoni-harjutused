#joosep alasoo
#18.12.23
#iseseisevtöö

def tervitus():
    print("Tere, maailm!")



def aasta_liblikas():
    aasta=2020
    liblikas="teelehe-mosaiikliblikas"
    lause_keskosa="aasta liblikas on:"
    lause=str(aasta)+lause_keskosa+liblikas
    print(lause)
"""
alus=float(input("pilvede aluse kõrgus (kilometrites):"))
def pilved(alus):
    if alus > 6:
        print("need on ülemised pilved")
    else:
        print("need ei ole ülemised pilved ")
"""



inimesed=float(input("mitu inimest on:"))
istekohtade_arv=float(input("mitu istekohta on bussis:"))
def buss(i,k):
    bussid= i % k
    if i == k:
        bussid=i//k
        viimases=i
    elif bussid > 0:
        bussid=i // k + 1
        viimases=i % k
    else:
        bussid=i//k
        viimases= k
    print(f"busse vaja {bussid}. \nViimases bussis {viimases} inimest")
buss(inimesed, istekohtade_arv)



