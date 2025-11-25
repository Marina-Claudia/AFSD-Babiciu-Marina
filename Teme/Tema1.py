import string
articol = """Fostul președinte al Consiliului Județean Cluj și fost deputat în Parlamentul României, Horea Uioreanu, a murit într-un cămin pentru vârstnici. El se afla încă din luna august în centrul Caro din Gilău."""
lungime = len(articol)
jumatate = lungime // 2
prima_parte = articol[:jumatate]
a_doua_parte = articol[jumatate:]
prima_parte = prima_parte.upper().strip()
a_doua_parte = a_doua_parte[::-1]
if len(a_doua_parte) > 0:
    a_doua_parte = a_doua_parte[0].upper() + a_doua_parte[1:]
for semn in [".", "?", "!", ","]:
    a_doua_parte = a_doua_parte.replace(semn, "")
rezultat = prima_parte + " " + a_doua_parte
print("Rezultatul final este:")
print(rezultat)