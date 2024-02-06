#massivid - array
#28.11.23-05.11.23
#joosep alasoo

"""
Vanused
Loo vanuste loend. Leia numbrite suurim ja väikseim arv, kogusumma, keskmine
Kasuta loendis olevate arvude väärtusi ning loo tärnide abil lintdiagramm.
"""
vanused=[12,13,14,15,16,17,18,4,53,67,87]
print(f"suurim arv on: {max(vanused)} ja väiksem arv on {min(vanused)}")
print(f"vanuste summa: {sum(vanused)}")
print(f"vanuste keskmine: {round(sum(vanused)/len(vanused),2)}")


for vanus in vanused:
    print(vanus*"*")








print("")
input()



"""
Duplikaadid
Tekita loend, kuhu oled lisanud meelega mõned ühesugused nimed.
Loo kood, mis ei väljasta kordusi.
"""


opilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']
uus_opilased=[]
for opilane in opilased:
    if opilane not in uus_opilased:
        uus_opilased.append(opilane)


print(uus_opilased)

print("")










input()













"""
Õpilased
Loo õpilaste nimedest loend. Programm lubab loendis olevaid nimesid muuta.
opilased = ['Juhan','Kati','Maarja','Mario','Mati']
"""

opilased = ['Juhan','Kati','Maarja','Mario','Mati']
jrk=1
for opilane in opilased:
    print(f"{jrk}.{opilane}")
    jrk+=1
valik=int(input("mitmendat nime tahad muuta:"))
uusnimi=input("lisa nimi:")
del opilased[valik-1]
opilased.insert(valik-1, uusnimi)


print(opilased)

input()

















"""
Nimede lisamine loendisse
Küsi kasutajalt viis nime. Salvesta need loendisse ja kuva tähestikulises järjekorras. Kuva eraldi viimati lisatud nimi.
"""

nimed = []

for i in range(5):
    nimi =input("lisa nimi:")
    nimed.append(nimi)
print("viimatu lisatud nimi:",nimed[-1])
nimed.sort()

print(nimed)