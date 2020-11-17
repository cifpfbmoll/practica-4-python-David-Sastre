# Practica 4
# Ejercicio 4
#Pida al usuario tres numeros y un cuarto numero, y compruebe si este ultimo\
#es divisor de los tres numeros primeros.

numero1=float(input("Indicame un numero. "))
numero2=float(input("Indicame un segundo numero. "))
numero3=float(input("Indicame un tercer numero. "))
numero4=float(input("Indicame un cuarto numero."))
if numero1%numero4==0 and numero2%numero4==0 and numero3%numero4==0:
    print(numero4, "es un numero divisor del resto de numeros")
else:
    print(numero4, "no es divisor")