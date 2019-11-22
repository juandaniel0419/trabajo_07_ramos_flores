#pedir nota de matematica, donde la nota debe estar entre 0 y 20
#mientras la nota ingresada no es valida debe pedirse otra vez
import os
nota=float(input(os.sys.argv[1]))
print(nota)
nota_invalida=(nota<=0 or nota>=20)

while(nota_invalida==True):
    nota=float(input(os.sys.argv[1]))
    nota_invalida=(nota<=0 or nota>=20)


print("fin del bucle")

