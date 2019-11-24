# Mostrar mensaje "Desea jugar apuesta" si o no ?
rpta=""
rpta_invalida=True
while(rpta_invalida):
    rpta=input("Desea jugar apuesta ? (si/no): ")
    rpta_invalida=(rpta != "si" and rpta != "no")
#fin_while
print("Fin del bucle")
print("La respuesta es :", rpta)

