#Date initiale
elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note = [9, 7, 10, 4, 8]

elev_nou = "Felix"
nota_elev_nou = 6
elev_de_sters = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]
    #Partea A
#A1)
for index1 in range(len(elevi)):
    for index2 in range(len(note)):
        if index1 == index2:
            print(elevi[index1],"are nota", note[index2])
#A2)
nota_maxima = max(note)
nota_minima = min(note)
for index1 in range(len(elevi)):
    for index2 in range(len(note)):
        if note[index2] == nota_maxima and index2 == index1:
            print(elevi[index1],"are nota", nota_maxima)