#joosep alasoo
#18.12.23
#iseseisevtöö2
import winsound
import random
"""
aratusde_arv=int(input("mitu korda sa tahad et äratus heliseks:"))
def aratus(nr):
    for i in range(nr):
        print("tõuse ja sära!")
"""

# ringid=int(input("ringide arv"))
# def porgandid(r):
#     joostud_ringid=0
#     porgandid=0
#     while joostud_ringid < r:
#         joostud_ringid+=1
#         if joostud_ringid%2==0:
#             porgandid+=joostud_ringid
#     print(f"jänkulaps saab:{porgandid} porgandit")
# porgandid(ringid)


# def taringud(arv):
#     for i in range(arv):
#         print(random.randint(1,6))
# taringud(6)




# def male(arv):
#     ruut=1
#     nisuterad=1
#     while ruut<arv:
#         nisuterad=nisuterad*2
#         ruut+=1
#     print(nisuterad)
# male(5)


mitu=int(input("mitu põialpoisi tahab õuna"))
def lumivalge(p):
    ounad=14
    for i in range(p):
        oun=random.randint(1,2)
        ounad-=oun
        print(oun)
    print(f"lumivalgekesele jäi {ounad} õuna")


lumivalge(6)





        