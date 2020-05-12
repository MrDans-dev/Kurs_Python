import random as rd
import string
import math

tablica1 = []
mieszana = ['Ala',1,1.5,3j,"F",hex(15)]
tablica3 =[]
lista1 = {}
slownik = {"1":"A","2":"B"}
for i in range(1,11):
    tablica1.append(i)

for i in range(10,0,-1):
    tablica3.append(i)

wynik = [i for i in tablica1]
#wynik = tablica1
for i in tablica1:
    print(i)

for i in range(0,len(tablica1)):
    print(tablica1[i])

print(wynik)
print()
print(tablica3)

print(tablica1) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tablica2 = [rd.randint(1,100) for i in range(1,11)] #Wpisywanie randomowych liczb do tablicy
print(tablica2)
#temp=[]
#for i in range(1,11):
#    if(i%2==0):
#        temp.append(i)
#tablica2=temp
tablica2 = [i for i in tablica2 if(i%2==0)]
print(tablica2)
for i in tablica2:
    print(i)

for i in range(0,len(tablica2)): #for(int i=0;i<5;i++)
    print(i , tablica2[i])

imie = "DanieL"
alfabet = [i for i in string.ascii_lowercase] #tablica z literami alfabetu
alfabet2 = string.ascii_lowercase
for i in range(0,len(imie)):
    for o in range(0,len(alfabet)):
        if(imie[i].lower() == alfabet[o]):
            print(o+1 , imie[i])


#Palindrom
slowo = "Kajak"
slowo2 = [i for i in slowo.lower()]
slowo = [i for i in slowo.lower()]
slowo.reverse()
if(slowo == slowo2):
    print("1")
else:
    print("0")



