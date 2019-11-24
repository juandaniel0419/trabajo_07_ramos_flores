# decodeficar el siguiente mensaje
# #=1
# !=2
# $=3
# %=te quiero
# /=dime que si por favor
# ()=quiero estar contigo
# ==vamos
# ¿=dias
# ¡=conociendonos

msg="%()=$!#¿¡/"
for signo in msg:
    if signo=="#":
        print("1")
    if signo=="!":
        print("2")
    if signo=="$":
        print("3")
    if signo=="%":
        print("te quiero ")
    if signo=="/":
        print("dime que si por favor")
    if signo=="()":
        print("quiero estar contigo")
    if signo=="=":
        print("vamos")
    if signo=="¿":
        print("dias")
    if signo=="¡":
        print("conociendonos")

# fin iteracion
print("fin del bucle")


