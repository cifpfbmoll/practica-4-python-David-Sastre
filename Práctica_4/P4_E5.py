# Practica 4
# Ejerciocio 5
# Pida al usuario un importe en euros y diga si el cajero automatico le \
#puede dar dicho importe utilizando el mismo billete y el mas grande\
#(recuerda que el billete puede ser de 500, 200, 100, 50, 20, 10 y 5).

dinero=int(input("Indica la cantidad de dinero que quieres sacar del banco. "))
if dinero%500==0:
    if dinero//500==1:
        print("El banco te devuelve 1 billete de 500")
    else:
        print("El banco te devuelve", dinero//500, "billetes de 500.")
elif dinero%200==0:
    if dinero//200==1:
        print("El banco te devuelve 1 billete de 200")
    else:
        print("El banco te devuelve", dinero//200, "billetes de 200.")
elif dinero%100==0:
    if dinero//100==1:
        print("El banco te devuelve 1 billete de 100")
    else:
        print("El banco te devuelve", dinero//100, "billetes de 100.")
elif dinero%50==0:
    if dinero//50==1:
        print("El banco te devuelve 1 billete de 50")
    else:
        print("El banco te devuelve", dinero//50, "billetes de 50.")
elif dinero%20==0:
    if dinero//20==1:
        print("El banco te devuelve 1 billete de 20")
    else:
        print("El banco te devuelve", dinero//20, "billetes de 20.")
elif dinero%10==0:
    if dinero//10==1:
        print("El banco te devuelve 1 billete de 10")
    else:
        print("El banco te devuelve", dinero//10, "billetes de 10.")
else:
    if dinero//5==1:
        print("El banco te devuelve 1 billete de 5")
    else:
        print("El banco te devuelve", dinero//5, "billetes de 5.")