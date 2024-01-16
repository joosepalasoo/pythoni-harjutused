#joosep alasoo
#10.01.24
#iseseisevtöö3
import datetime
paev=datetime.datetime.now().day
#tahvli juurde
fail=open("nimekiri.txt", encoding="utf-8")
nr=1
for nimi in fail:
    if nr == paev:
        print(nimi,end="")
    nr+=1





# #jukebox
# muusika=input("anna faili nimi:")
# fail=open(muusika, encoding="utf-8")
# print("muusika valik:")
# nr=1
# for i in fail:
#     print(f"{nr}.{i}",end="")
#     nr+=1
# valik=int(input(" vali laulu number:"))


# fail.seek(0) #mine faili algusese
# nr=1
# for i in fail:
#     if nr == valik:
#         print(i)
#     nr+=1






#sisetulekud

# fail=open("konto.txt")
# for i in fail:
#     if float(i) > 0:
#         print(i,end="")



# #rebased
# fail =open("rebased.txt",encoding="utf-8")
# vastuvoetud=[]
# for rida in fail:
#     vastuvoetud.append(int(rida))


# print(vastuvoetud)
# fail.close()




