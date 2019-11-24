####imprimir los numeros pares del 40 al 60
n=40
h = ''
while n <= 60:
    if n%2 == 0:
        h += ' %i' % n
    n += 1
####fin while
print(h)
print("fin del bucle")
