#ingresar la edad de una persona y luego pedir su año de nacimiento, mientras su año de nacimiento sea invalido, volver a pedirlo
import os
edad=int(input(os.sys.argv[1]))
año=int(input(os.sys.argv[2]))


edad_invalida=(edad<=0 or edad>100)
año_invalida=(año<=1900 or año>2019)

while(edad_invalida==True):
    edad=int(input(os.sys.argv[1]))
    edad_invalida=(edad<=0 or edad>100)

while(año_invalida==True):
    año=int(input(os.sys.argv[2]))
    año_invalida=(año<=1900 or año>2019)

#fin_while
print("fin del bucle")
