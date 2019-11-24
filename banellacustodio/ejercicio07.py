###Calcular e imprimir los numeros de 5 en 5 del 100 al 20 en forma decreciente
n = 100
h = ''
while n >= 20:
    h += ' %i' % n
    n -= 5
###fin while
print(h)
print("fin del bucle")