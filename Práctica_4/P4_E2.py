# Practica 4
# Ejercicio 2
# Pida al usuario 5 numeros y diga si estos estaban en orden decreciente\
# creciente o desordenados.


print("Indica cinco numeros y te dire de que forma estan ordenados.")
numero1=float(input())
numero2=float(input())
numero3=float(input())
numero4=float(input())
numero5=float(input())
if numero1>numero2>numero3>numero4>numero5:
    print("Los numeros estan ordenados de forma decreciente.")
elif numero1<numero2<numero3<numero4<numero5:
    print("Los numeros estan ordenados de forma creciente.")
else:
    print("Los numeros estan desordenados.")