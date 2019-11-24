nota=int(input("ingrese la nota del alumno:"))
print(nota)
nota_invalida=(nota<0 or nota>20)

###validar que la nota este entre 0 y 20
while (nota_invalida==True):
    nota=int(input("ingrese nota:"))
    nota_invalida=(nota<0 or nota>20)
#fin while
print("fin del bucle")