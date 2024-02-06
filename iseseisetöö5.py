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
jaanuar -16 -12 -15 -20 0 -1 -20 -2 -20 -14 -18 -8 2 -1 -14 -7 -15 -17 -6 -17 -17 -7 0 3 -20 -17 -15 -8 -12 3
	veebruar -9 -2 -7 1 -16 -19 -19 -11 -16 -15 -9 -2 -16 -4 -20 -5 -6 -17 -5 0 -16 2 0 -20 -16 -2 -18
	mĆ¤rts 2 -9 -1 -3 -6 -2 1 -2 -3 -9 -1 -4 0 -6 -7 1 0 2 -5 -10 2 -7 -3 2 -10 2 -9 -8 -5 -2
	aprill -5 0 10 -9 0 -9 -8 6 -5 3 -1 4 9 -1 2 0 10 0 5 0 -10 0 6 3 -6 -2 -10 -8 -2
	mai 12 5 8 -1 -2 4 10 -1 7 15 7 3 6 4 10 9 13 6 14 10 14 2 6 12 15 2 14 11 9 1
	juuni 12 5 17 6 10 14 9 7 15 23 29 11 16 18 9 25 14 8 16 22 19 22 23 18 16 16 26 24 22
	juuli 15 8 21 28 18 13 9 9 8 6 8 12 12 29 28 20 6 9 12 8 14 18 14 13 23 6 24 24 17 20
	august 7 6 5 19 18 18 17 20 15 11 7 10 13 12 20 11 10 14 18 14 24 6 17 16 6 17 5 13 11
	september 21 19 21 9 13 18 6 6 20 7 25 13 8 9 14 16 19 10 7 25 7 17 16 15 17 18 15 9 19
	oktoober 2 2 1 5 -2 5 5 2 2 2 1 -2 1 -2 0 -2 5 4 0 1 -1 2 0 2 2 2 -1 1 4 -1
	november -6 -7 -2 -7 -2 -4 0 -7 -8 -6 0 -9 -2 -3 -2 0 -8 -2 -5 -2 -5 -8 -10 0 -2 -9 -9 -7 -1
	detsember -15 2 -11 -14 -15 -5 -5 -18 -18 -19 0 0 2 -7 -16 -7 -4 -1 -1 -16 -18 -10 -3 -19 -6 -16 -16 -8 -2 -18
"""
def Temperatuurid():
    kuud=["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    temp=[[-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3],
          [-9,-2,-7,1,-16,-19,-19,-11,-16,-15,-9,-2,-16,-4,-20,-5,-6,-17,-5,0,-16,2,0,-20,-16,-2,-18],
          [2,-9,-1,-3,-6,-2,1,-2,-3,-9,-1,-4,0,-6,-7,1,0,2,-5,-10,2,-7,-3,2,-10,2,-9,-8,-5,-2],
          [-5,0,10,-9,0,-9,-8,6,-5,3,-1,4,9,-1,2,0,10,0,5,0,-10,0,6,3,-6,-2,-10,-8,-2],
          [12,5,8,-1,-2,4,10,-1,7,15,7,3,6,4,10,9,13,6,14,10,14,2,6,12,15,2,14,11,9,1],
          [12,5,17,6,10,14,9,7,15,23,29,11,16,18,9,25,14,8,16,22,19,22,23,18,16,16,26,24,22],
          [15,8,21,28,18,13,9,9,8,6,8,12,12,29,28,20,6,9,12,8,14,18,14,13,23,6,24,24,17,20],
          [7,6,5,19,18,18,17,20,15,11,7,10,13,12,20,11,10,14,18,14,24,6,17,16,6,17,5,13,11],
          [21,19,21,9,13,18,6,6,20,7,25,13,8,9,14,16,19,10,7,25,7,17,16,15,17,18,15,9,19],
          [2,2,1,5,-2,5,5,2,2,2,1,-2,1,-2,0,-2,5,4,0,1,-1,2,0,2,2,2,-1,1,4,-1],
          [-6,-7,-2,-7,-2,-4,0,-7,-8,-6,0,-9,-2,-3,-2,0,-8,-2,-5,-2,-5,-8,-10,0,-2,-9,-9,-7,-1],
          [-15,2,-11,-14,-15,-5,-5,-18,-18,-19,0,0,2,-7,-16,-7,-4,-1,-1,-16,-18,-10,-3,-19,-6,-16,-16,-8,-2,-18]]

    max_temp = float('-inf')
    max_temp_kuup = ""
    
    for i in range(len(kuud)):
        for j in range(len(temp[i])):
            if temp[i][j] > max_temp:
                max_temp = temp[i][j]
                max_temp_kuup = f"{j+1}. {kuud[i]}"
    
    print(f"kuumim kuupäev on: {max_temp_kuup} ja temperatuur sellel päeval oli {max_temp} kraadi.")
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
        item=input("lisa toode(kui jätad välja tühjaks siis kuvatakse sisestatud tooted ): ")
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