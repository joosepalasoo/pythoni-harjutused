#joosep alasoo
#10.01.24
#iseseisevtöö4

#mündid

def pronksikarva_summa(f):
    kassa=0
    fail=open("myndid.txt")
    for mynt in fail:
         if int(mynt)<10:
            print(mynt, end="")
            kassa+=int(mynt)
    print("\nkassas: ", kassa)















# #tervitused
# kylalised=8
# def tervitus(n):
#     print('võõrustaja: "tere!"')
#     print(f"täna {n}. kord tervitada")
#     print('külaline: "tere, suur tänu kutsumast"')
# for i in range(kylalised):
#     tervitus(i+1)








# #peoeelarve
# def eelarve(kylalised):
#     summa=kylalised * 10 + 55
#     return summa
# palju= int(input("mitu kutsutud: "))
# palju2= int(input("mitu tuleb: "))
# print((f"maksimaalne eelarve:{eelarve(palju)}"))
# print(f"minimaalne eelarve:{eelarve(palju2)}")










# #õunamahl

# def mahlapakide_arv(kg):
#     pakid=round(kg * 0.4/3)
#     return pakid

# kogus=float(input("õunte kogus: "))
# print(mahlapakide_arv(kogus))









# #suured tähed
# def banner(t):
#     print(t.upper())
# ask=int(input("mitu korda: "))
# ask2=input("reklaamlause")
# for i in range(ask):
#     banner(ask2)