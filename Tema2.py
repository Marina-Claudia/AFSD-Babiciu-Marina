#Date initiale
elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note = [9, 7, 10, 4, 8]

elev_nou = "Felix"
nota_elev_nou = 6
elev_de_sters = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]

    #Partea A
#A1.
for index1 in range(len(elevi)):
    for index2 in range(len(note)):
        if index1 == index2:
            print(elevi[index1],"are nota", note[index2])
#A2.
nota_maxima = max(note)
nota_minima = min(note)
for index1 in range(len(elevi)):
    for index2 in range(len(note)):
        if note[index2] == nota_maxima and index2 == index1:
            print("Elevul/eleva", elevi[index1],"are nota maxima:", nota_maxima)
        if note[index2] == nota_minima and index2 == index1:
            print("Elevul/eleva", elevi[index1],"are nota minima:", nota_minima)
#A3.
suma_note = float(sum(note))
media_aritmetica_note = suma_note / float(len(note))
print('%.2f'%(media_aritmetica_note))
#A4.
print("Elevii care au promovat sunt:")
for index in range(len(note)):
    for index_1 in range(len(elevi)):
        if note[index] >= 5 and index == index_1:
            print(elevi[index_1])
print("=================================")
    #Partea B
#B5.
print("Dupa adunarea unui punct fiecarei note, notele sunt:")
for index1 in range(len(note)):
    if note[index1] + 1 <= 10:
        note[index1] += 1
        print(note[index1])
# Date initiale
    elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
    note = [9, 7, 10, 4, 8]

    elev_nou = "Felix"
    nota_elev_nou = 6
    elev_de_sters = "Darius"

    interogari_nume = ["Ana", "Mara", "Elena", "stop"]

    absente = [1, 0, 2, 3, 0]
#B6.
elevi.append(elev_nou)
note.append(nota_elev_nou)
print(elevi)
print(note)
#B7.
for index1 in range(len(elevi)):
    for index2 in range(len(note)):
        if index1 == index2 and elevi[index1] == elev_de_sters:
            elevi.remove(elev_de_sters)
            note.remove(note[index2])
print(elevi)
print(note)
#B8.
for index1 in range(len(elevi)):
    for index2 in range(len(note)):
        if index1 == index2:
            print(elevi[index1],"are nota", note[index2])
print("=================================")
    #Partea C
#C9.
index = 0
while interogari_nume[index] != "stop":
    if interogari_nume[index] in elevi:
        for index2 in range(len(note)):
            if index2 == index:
                print(interogari_nume[index], "are nota", note[index2])
    index += 1
if index == 0:
    print('nu s-au gasit elevii in lista')
#C10.
#1.
print("=================================")
numar_elevi_promovati = 0
numar_elevi_respinsi = 0
for index1 in range(len(elevi)):
    for index2 in range(len(note)):
        if index1 == index2 and note[index2] >= 5:
            numar_elevi_promovati += 1
        elif index1 == index2 and note[index2] < 5:
            numar_elevi_respinsi += 1
print(numar_elevi_promovati, "elevi au promovat")
print(numar_elevi_respinsi, "sunt respinsi")
#2.
print("=================================")
elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note = [9, 7, 10, 4, 8]
numar_elevi_promovati = 0
numar_elevi_respinsi = 0
for index1 in range(len(elevi)):
    for index2 in range(len(note)):
        if index1 == index2 and note[index2] >= 5:
            numar_elevi_promovati += 1
        elif index1 == index2 and note[index2] < 5:
            numar_elevi_respinsi += 1
print(numar_elevi_promovati, "elevi au promovat")
print(numar_elevi_respinsi, "sunt respinsi")
#C11.
note = [9, 7, 10, 4, 8]
lista_note = []
if note:
    for element in note:
        if element >= 5:
            lista_note = [element]
print(lista_note)
suma_notelor = sum(lista_note)
media_aritmetica_note = suma_notelor / len(lista_note)
print(media_aritmetica_note)
