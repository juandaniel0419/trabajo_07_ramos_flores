# mostrar "peso excesivo", cuando sobrepasan los 500kg
import os
peso=float(input(os.sys.argv[1]))
print(peso)

peso_erreneo=(peso<0 or peso>1000)

while(peso_erreneo==True):
    peso_erreneo=(peso<0 or peso>1000)
    peso = float(input(os.sys.argv[1]))

#fin_while
print("fin del bucle")





