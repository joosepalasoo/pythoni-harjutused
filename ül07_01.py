import math
#funktsioonid
#05.11.23
#joosep alasoo


"""
1. Koosta funktsioon, mille väljakutsumisel tevitab kasutajat tema enda nimega
    tervita('Mario')    
2. Täienda eelmist funktsiooni nii, mis tervitab mind eesti või inglise keeles. Vaikimisi tervitatakse mind hoopis saksa keeles.
    tervita('Mario', et)    
3. Koosta ruumalade leidmise programm. Kasutajalt küsitakse, millise kujundi ruumala on vaja leida ja siis vajalikke argumente. Kasutada tuleb funktsioone. Tore, kui programm ei lõpetaks kohe töö vaid lubab valida teisi ruumalasid.
    ********** LEIAME RUUMALA **********
    Vali kujund
    1 Kuup
    2 Kera
    3 Koonus
    4 Silinder
    Sisesta soovitud kujundi number: 2
    Valisid kera. Sisesta kera raadius: 10
    Kera ruumala on: 4188.79
"""










def tervita(nimi,keel="de"):
    if keel == "en":
        print(f"hi {nimi}!")
    elif keel == "et":
        print(f"tere {nimi}!")
    else:
        print(f"hallo {nimi}!")


tervita("joosep")
tervita("joosep","en")



def kuup(a,b,c):
    v=a*b*c
    print(f"kuubi ruumala on: {v}")

def kera(r):
    b=round(4*math.pi*r**2,2)
    print(f"kera ruumala on:{b}")

def koonus():
    print("koonus")

def silinder():
    print("silinder")



loop=1
print("leiame ruumala")
while loop == 1:
    print("vali kujund\n1 kuup\n2 kera\n3koonus\n4 silinder\n5 exit")
    valik=int(input("tee valik:"))

    if valik == 1:
        a=int(input("külg 1: "))
        b=int(input("külg 1: "))
        c=int(input("külg 1: "))
        kuup(a,b,c)
    elif valik==2:
        r=int(input("sisesta kera raadius:"))
        kera(r)
    elif valik==3:
        koonus()
    elif valik==4:
        silinder()
    else:
        loop=0
    print("-----------")

    print("bye bye")

