# decodificar el siguiente mensaje
# a= hola como estas
# b= buenos dias
# c= ¿quieres salir?
# d= ¿que te gusta comer?
# f= bueno bye mañana

msg="bacdf"

for letra in msg:
    if letra=="a":
        print("hola como estas")
    if letra=="b":
        print("buenos dias")
    if letra=="c":
        print("¿quieres salir?")
    if letra=="d":
        print("¿que te gusta comer?")
    if letra=="f":
        print("bueno bye, hasta mañana")

#fin iteracion
print("fin del bucle")