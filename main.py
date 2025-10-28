#21.10.2025
#if
from conda_build.inspect_pkg import print_linkages
numar = 0
if numar > 0:
       print("numarul este pozitiv")
elif numar < 0:
       print("numarul este negativ")
else:
       print("numarul este 0")
#ex 1) se da o nota, sa se afiseze daca a promovat sau nu
nota = 8
if nota >= 5:
       print("promovat cu nota ")
       print(nota)
else:
       print("nepromovat")
#ex 2) sa se afiseze daca nr este par sau impar
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
#ex 1) cate cifre are un numar
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
#28.10.2025
# ~LISTE~
lista_de_numere = [10, 20, 30, 40, 50]
lista_diversa = [1, "text", 3.14, True, [1, 2, 3]]
       #indexarea elementelor din lista
       #primul element are indexul 0
print(lista_de_numere[0])
print(lista_de_numere[-1])
       #segmentare/ slicing liste
sublista = lista_de_numere[1:4:2]
print(sublista)
       #separatorii + si *
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
print(lista_1+lista_2)
       #inmultirea cu un numar intreg = repetare
print(lista_1*3)
       #adaugarea element in lista
       #append(element) = adauga elementul la finalul listei
lista_1.append(10)
print(lista_1)
       #insert(index, element)
lista_1.insert(2, 77)
print(lista_1)
       #stergere element din lista
       #metoda 1: pop(index) = sterge si returneaza elementul de la indexul dat
lista_1.pop(2)
print(lista_1)
element_sters = lista_1.pop(2)
print(element_sters)
       #metoda 2: remove(element) = sterge prima aparitie a elementului dat
lista_1 = [1, 2, 3, 2, 4, 3]
lista_1.remove(3)
print(lista_1)
       #gasirea elementelor din lista
       #index(element) = returneaza pozitia primei aparitii a elementului dat
lista_1 = [1, 2, "3", 2, 4, 3]
index_element = lista_1.index(2)
print(index_element)
       #count(element) = returneaza de cate ori apare elementul in lista
print(lista_1.count(2))
       #sort() = sorteaza lista in ordine crescatoare
lista_de_numere = [50, 20, 10, 40, 30]
print(lista_de_numere)
lista_de_numere.sort()
print(lista_de_numere)
lista_de_numere.sort(reverse=True)
print(lista_de_numere)
print("=======================")
       #sorted(lista) = returneaza o alta lista cu elem. sortate
lista_de_numere = [50, 20, 10, 40, 30]
print(lista_de_numere)
lista_sortata = sorted(lista_de_numere)
print(lista_sortata)
print(lista_de_numere)
       #len(lista) = returneaza nr. de elem. din lista
print(len(lista_de_numere))
       #max(lista) = returneaza valoarea maxima
print(max(lista_de_numere))
       #min(lista) = returneaza valoarea minima
       #sum(lista) = returneaza suma elem. din lista
       #media aritmetica a elem. din lista
media = sum(lista_de_numere) / len(lista_de_numere)
print(media)
print('-------------------------')
       #parcurgeri de liste
       #metoda 1: for element in lista
lista_de_numere = [10, 20, 30, 40, 50]
for element in lista_de_numere:
       print(element)
#ex 1) afisati elem. mai mari decat 30
for element in lista_de_numere:
       if element > 30:
              print(element)
       #metoda 2: for index in range(len(lista))
print('--------------------------------')
lista_de_numere = [101, 224, 32, 436, 50, 501, 222, 20]
for index in range(len(lista_de_numere)):
       print(index,",",lista_de_numere[index])
print("--------------------------------")
#ex 2) afisati elementele pare de pe pozitiile impare
for index in range(len(lista_de_numere)):
              # pozitia e index
              # valoarea e lista_de_numere[index]
       if index % 2 == 1 and lista_de_numere[index] % 2 == 0:
              print(lista_de_numere[index])
       #metoda 3: while
print("=====================================")
lista_de_numere = [10, 20, 30, 40, "stop", 50]
index= 0
while lista_de_numere[index] != "stop":
       print(lista_de_numere[index])
       index += 1
