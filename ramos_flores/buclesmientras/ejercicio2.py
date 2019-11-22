#mostrar "accseo denegado mientras la clave no sea "2019"
import os
clave=int(input(os.sys.argv[1]))
print(clave)

clave_incorrecta=(clave!=2019)
print("acceso denegado")

while(clave_incorrecta==True):
    clave=int(input(os.sys.argv[1]))
    clave_incorrecta=(clave!=2019)

print("fin del bucle")