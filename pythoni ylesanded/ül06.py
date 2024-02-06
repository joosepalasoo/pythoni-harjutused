#teksti failid
#05.11.23
#joosep alasoo



"""
1. Sinu ülesanne on koostada programm, mis kuvab pooliitikud inimsilmale sõbralikus vaates.

2. Täienda eelmist programmi nii, et kuvataks kui palju on nimekirjas kodanikke Reformierakonnast ja kui palju Keskerakonnast
    Reformikaid: 3
    Kesikuid: 1
3.Täienda programmi veelgi ja leia, kui palju oli erinevaid erakondi kokku.

    Erakondi kokku: 4
4. Viimase täiendusena salvestab sinu programm ainult poliitikute nimed uude faili (loetavalt).
"""

fail=open("s6pru_l6ustaraamatus.txt","r")
erakonad=[]
re=0
ke=0
for rida in fail:
    #enimi,perenimi,erak,sobrad=rida.split(" ")
    politik=rida.split(" ")
    print(f"{politik[0]:10} {politik[1]:10} {politik[2]:4} {politik[3]}",end="")
    if politik[2]=="RE":
        re+=1 #re=re+1
    elif politik[2]=="KE":
        ke+=1
    if politik[2] not in erakonad:
        erakonad.append(politik[2])
    
    with open("politikud.txt","a") as kirjutamiseks:
        kirjutamiseks.write(politik[0]+" "+politik[1]+"\n")

print()
print(f"reformikad: {re}\nkesikuid:{ke}")
print(f"erakondi kokku: {len(erakonad)}")


fail.close()











