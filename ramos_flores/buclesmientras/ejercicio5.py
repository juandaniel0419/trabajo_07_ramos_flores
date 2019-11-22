#moatrar el mensaje "ingrese el color (1=blanco , 2=negro), mientras la respuesta ingresada
#se un numero distinto a 1 ö 2, mostrar ingrese color
import os
color=int(input(os.sys.argv[1]))
color_erroneo=(color!=1 and color!=2)

while(color_erroneo==True):
    color=int(input(os.sys.argv[1]))
    color_erroneo=(color!= 1 and color!= 2)


print("fin del bucle")


