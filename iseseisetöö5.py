#iseseisevtöö5
#joosep alasoo
#16.01.24
import random

"""
17. Email
	Kasutaja lisab emaili kujul enimi.pnimi@server.com
	Programm kontrollib kas email on sisestatud Ćµigesti
	Programm tĆ¼keldab selle ja vĆ¤ljastab lause: Tere enimi, sinu email on server serveris ja domeeniks on sul com
"""

def email_kontroll():
    email=input("sisesta email: ")
    if "@" in email:
        email=email.split("@")
        eesnimi=email[0].split(".")[0]
        domain=email[1].split(".")
        print(f"tere {eesnimi}, sinu email on serveris {domain[0]} ja domeeniks on sul {domain[1]}")
    else:
        print("vale email")
email_kontroll()

input()








































"""
Temperatuurid - Programm peab tĆ¶Ć¶tlema Ć¼he aasta kĆµigi pĆ¤evade temperatuure. 
Kirjutada programm, mis leiab kuude kaupa, mitmendal kuupĆ¤eval oli kĆµige soojem. 
VĆ¤ljasta kuupĆ¤ev ja vastav temperatuur. (Kui sama temperatuuriga oli mitu pĆ¤eva, vĆ¤ljasta vĆ¤hemalt Ć¼ks)
"""
def Temperatuurid():
    kuud = []
    kuud.append([]) #jaanuar
    kuud.append([]) #veebruar
    kuud.append([]) #märts
    kuud.append([]) #aprill
    kuud.append([]) #mai
    kuud.append([]) #juuni
    kuud.append([]) #juuli
    kuud.append([]) #august
    kuud.append([]) #september
    kuud.append([]) #oktoober
    kuud.append([]) #november
    kuud.append([]) #detsember
    kuud.append([]) #aasta
    for i in range(1, 13):
        kuud[12].append(0)
    for i in range(1, 32):
        kuud[0].append(random.randint(-25, 25))
        kuud[1].append(random.randint(-25, 25))
        kuud[2].append(random.randint(-25, 25))
        kuud[3].append(random.randint(-25, 25))
        kuud[4].append(random.randint(-25, 25))
        kuud[5].append(random.randint(-25, 25))
        kuud[6].append(random.randint(-25, 25))
        kuud[7].append(random.randint(-25, 25))
        kuud[8].append(random.randint(-25, 25))
        kuud[9].append(random.randint(-25, 25))
        kuud[10].append(random.randint(-25, 25))
        kuud[11].append(random.randint(-25, 25))
    for i in range(0, 12):
        kuud[12][i] = sum(kuud[i]) / len(kuud[i])
    
    # väljastab temperatuurid
    months = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    for i in range(0, 12):
        print(months[i], end=" ")
        for temp in kuud[i]:
            print(temp, end=" ")
        print()
    
    # leiab kõige soojema päeva
    for i in range(0, 12):
        max_temp = max(kuud[i])
        max_temp_index = kuud[i].index(max_temp) + 1
        print(months[i], max_temp_index, max_temp)
Temperatuurid()


input()


#nais cood mees ja kui pärast pushin ikka saab mario pahaseks




















"""
13. Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris vĆµi paaritu
	kuvatakse korrektne arusaadav kĆ¼simus ja  vastus - 1p
	eelnev kontroll, kas kasutaja ei lisanud arvu vĆµi pani nulli - 2p
	kood mis teavitab paaris vĆµi paaritust arvust - 2p
	kuvatakse programmi pealkiri - 1p
"""

def paaritu_paaris():
    #küsib inimeselt arvu
    arv=int(input("sisesta arv: "))
    #kontrollib kas arv on paaris või paaritu
    if arv==0:
        print("null")
    elif arv%2==0:
        print("paaris")
    else:
        print("paaritu")
paaritu_paaris()







input()



















"""
11. Salakeel
sinu programm küsib kasutajalt, kas ta soovib salakeelt luua või tõlkida - 1p
kasutaja sisestab tavalise sõna, mis muudetakse salakeeleks - 1p
kasutaja sisestab salakeeles sõna, mis teisendatakse jälle normaalseks - 1p
kood kommenteeritud - 1p
"""

def salakeel(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

choice = input("vajuta e et teha krüptitud sõna või d et dekrüptida sõna: ")
word = input("sisesta sõna: ")
shift = int(input("sisesta tähtede liikumis arv: "))

if choice == 'e':
    kryptitud_sõna = salakeel(word, shift)
    print(f"krüptitud sõna: {kryptitud_sõna}")
elif choice == 'd':
    dekryptitud_sõna = salakeel(word, -shift)
    print(f"dekrüptitud sõna: {dekryptitud_sõna}")
else:
    print("vale valik lammas!")
















input()






"""
9. Emaili kontroll
	kasutaja lisab emaili kujul enimi.pnimi@server.com - 1p
	programm kontrollib kas email on sisestatud Ćµigesti - vĆ¤hemalt @-mĆ¤rgi kontroll - 1p
	programm tĆ¼keldab selle ja vĆ¤ljastab lause: ā€Tere enimi, sinu email on server serveris ja domeeniks on sul comā€™ - 1p
	kasutajalt kĆ¼situd kĆ¼simused on selgelt Ć¼heselt mĆµistetavad - 1p
	kood kommenteeritud - 1p
"""

def email():
    #küsib kasutajalt emaili
    email=input("sisesta email: ")
    #kontrollib kas email on sisestatud õigesti
    if "@" in email:
        #tükeldab emaili
        email=email.split("@")
        #tükeldab emaili teise osa
        domain=email[1].split(".")
        #väljastab lause
        print(f"tere {email[0]}, sinu email on serveris {domain[0]} ja domeeniks on sul {domain[1]}")
    else:
        #kui email on vale siis väljastab veateate
        print("vale email")
#käivitab funktsiooni
email()

input()





















"""
7. Eurokalkulaator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK vĆµi EEK->EUR.
	kuvatakse korrektne arusaadav kĆ¼simus ja vastus - 1p
	kuvatakse veateade, kui kasutaja tegi valiku valesti - 1p
	kĆ¼sitakse valuuta kogust ja tehakse arvutused - 2p
	kood kommenteeritud - 1p
"""
def eurokalkulaator():
    #alustab loopi
    while True:
        #väjastab valikud kasutajale
        print("1. EUR->EEK")
        print("2. EEK->EUR")
        print("3. EXIT")
        #küsib kasutaja valikut
        valik=int(input("vali: "))
        if valik==1:
            #küsib kasutajalt summat mida vahetada
            summa=int(input("summa: "))
            #kuvab vahetatud summa kroonides
            print(f"{summa} eurot on {summa*15.6466} krooni")
        elif valik==2:
            summa=int(input("summa: "))
            #kuvab vahetatud summa eurodes
            print(f"{summa} krooni on {summa/15.6466} eurot")
            #kui kasutaja küsib 3 valikut siis:
        elif valik==3:
            #lõpetab loopi
            break
            #kui kasutaja küsib muud valikut siis mida ei eksisteeri:
        else:
            #kuvatakse veateade
            print("vale valik loll lammas")
#käivitab funktsiooni
eurokalkulaator()


input()












"""
5. Shopping List
Create a program that will keep track of items for a shopping list. The program should keep asking for new items until nothing is entered (no input followed by enter/return key).
 The program should then display the full shopping list.
"""
def shopping():
    shoppinglist=[]
    while True:
        item=input("lisa toode: ")
        if item=="":
            break
        else:
            shoppinglist.append(item)
    print(shoppinglist)
shopping()


input()



















"""
3. Positiivsed ja negatiivsed
	tee kaks loendit positiivsete ja negatiivsete arvude hoidmiseks 1p
	kasutaja sisestab 5 arvu ja programm tuvastab, kumba loendisse selle lisab 2p
	nulli lisamisel ei tehta midagi 1p
	vĆ¤ljasta mĆµlemad loendit 1p
"""
def posneg():
    pos=[6,5,3,4,8,10,3]
    neg=[-7,-5,-3,-4,-8,-10,-3]
    korrad=0
    while korrad<5:
        arv=int(input("sisesta arv: "))
        if arv==0:
            print("ära sisesta nulli")
        else:
            if arv>0:
                pos.append(arv)
            elif arv<0:
                neg.append(arv)
            korrad+=1
    print(pos)
    print(neg)
posneg()





input()








"""1. Korrutamise kontrollimine
	programm esitab korrutustehte 1p
	ootab kasutajalt vastuse sisestamist 1p
	kontrollib vastuse Ćµigsust 1p
	vĆ¤ljastab, kas vastus oli Ćµige vĆµi vĆ¤Ć¤r. 1p
	kokku antakse lahendamiseks 10 Ć¼lesannet. 1p
    """
arv1=random.randint(1,100)
arv2=random.randint(1,100)

def korutamine(arv1,arv2):
    print(f"{arv1} * {arv2}")
    vastus=int(input("vastus: "))
    if vastus==arv1*arv2:
        print("õige")
    else:
        print("vale")
for i in range(10):
    korutamine(arv1,arv2)
    arv1=random.randint(1,100)
    arv2=random.randint(1,100)
korutamine(arv1,arv2)