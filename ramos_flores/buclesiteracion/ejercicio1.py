# Decodificar mensaje encriptado
# A = Hola
# B = Que tal
# F = Te estoy esperando
# R = Chao
msg="AABFR"

for letra in msg:
    if letra == "A":
        print("Hola")
    if letra == "B":
        print("Que tal")
    if letra == "F":
        print("Te estoy esperando")
    if letra == "R":
        print("Chao")
#fin_iterador

print("Fin del bucle")
