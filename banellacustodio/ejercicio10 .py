###Programa que imprima los numeros impares desde el 100 hasta el 1 y calcule su suma
n = 100
h = 0
while n >= 1:
    if n%2 != 0:
        print (n),
        h += n
    n -= 1
###fin while
print('y su suma es: %i' % h)
print("fin del bucle")
