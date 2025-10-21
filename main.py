#if
from conda_build.inspect_pkg import print_linkages
numar = 0
if numar > 0:
       print("numarul este pozitiv")
elif numar < 0:
       print("numarul este negativ")
else:
       print("numarul este 0")
#se da o nota, sa se afiseze daca a promovat sau nu
nota = 8
if nota >= 5:
       print("promovat cu nota ")
       print(nota)
else:
       print("nepromovat")
#sa se afiseze daca nr este par sau impar
nr = 7
if nr%2==0:
       print("nr este par")
else:
       print("nr este impar")
# structuri repetitive while si for
# 1) while: nu stim nr de pasi
while(nr > 0):
       nr -= 1
       print(nr)
#cate cifre are un numar
numar= 9584739211100293
numar_cifre = 0
while numar > 0:
       numar = numar // 10
       numar_cifre += 1
print (numar_cifre)
# 2) for: range (start, stop, pas) -genereaza secventa de nr pentru for
for i in range(0, 100, 2):
       print(i, end=" ")
print()
#for in sir de caractere - string
text= "Hello world!"
for caracter in text:
       print(caracter)
print("------------------------")
#parcurgerea caracterelor cu index (pozitie)
print(text[1])
for index in range (0, len(text), 1):
       print (text[index])
#range are valori predefinite (start=0 si pas=1)
#ex: range(10) = range (0, 10, 1)
print("======================================")
#afisam vocalele dintr-un text
text= "Azi este o zi frumoasa"
vocale= "aeiouAEIOU"
for index in range (len(text)):
       print(text[index])
print("")
for index in range(len(text)):
       if text[index] in vocale:
              print(text[index])
text1 = ""
text2 = "Hello"
if text1:
       print("sirul este plin")
else:
       print("sirul este gol")
print("======================")
#numararea vocalelor dintr-un sir de caractere
text= "Azi este o zi frumoasa"
vocale= "aeiouAEIOU"
nr_vocale = 0
for caracter in text:
       if caracter in vocale:
              nr_vocale += 1
print(nr_vocale)