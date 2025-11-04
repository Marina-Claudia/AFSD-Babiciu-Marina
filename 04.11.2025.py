#FUNCTII
from math import floor


def nume_functie(parametrii):
    #bloc de cod
    return nume_functie(parametrii)

def functie_fara_parametrii():
    print("Functie fara parametrii")

def functie_test(a, b):
    suma = a + b
    return suma
if __name__ == "__main__":
    s = functie_test(10, 20)
    print(functie_test(12, 90))
    print(s)
#Functie pentru a verifica daca un nr e prim
#parametru: numar
#returneaza: true(nr prim) / false(nu e nr prim)
#verificam numarand divizorii
def este_prim(numar):
    nr_divizori = 0
    for i in range(1, numar + 1):
        if numar % i ==0:
            nr_divizori += 1
    if nr_divizori == 2:
        return True
    else:
        return False
if __name__ == "__main__":
    print(este_prim(11))

#parametrii cu ** kwargs
def afisare_informatii(** kwargs):
    print(kwargs)
    for cheie, valoare in kwargs.items():
        print(cheie, valoare)
def varste(a,b):
    if a > b:
        x = a - b
        mesaj_1 = "Primul copil este mai mare cu "
        mesaj_2 = " ani"
        mesaj = mesaj_1 + str(x) + mesaj_2
    elif a < b:
        x = b - a
        mesaj_1 = "Al doilea copil este mai mare cu "
        mesaj_2 = " ani"
        mesaj = mesaj_1 + str(x) + mesaj_2
    elif a == b:
        mesaj = "Copiii au varste egale"
    return mesaj
if __name__ == "__main__":
    print(varste(5, 6))