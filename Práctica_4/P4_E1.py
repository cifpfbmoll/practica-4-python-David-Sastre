# Practica 4
#   Ejercicio 1
#       Pida al usuario 5 numeros y diga cual es el mayor y cual el menor.

print("Por favor introduzca cinco numeros")
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
if (a>b and a>c and a>d and a>e):
     ("El numero mas grande es",a)
elif (b>a and b>c and b>d and b>e):
    print ("El numero mas grande es",b)
elif (c>a and c>b and c>d and c>e):
    print ("El numero mas grande es",c)
elif (d>a and d>b and d>c and d>e):
    print ("El numero mas grande es",d)
elif (e>a and e>b and e>c and e>d):
    print ("El numero mas grande es",e)
if (a<b and a<c and a<d and a<e):
    print ("El numero mas pequeno es",a)
elif (b<a and b<c and b<d and b<e):
    print ("El numero mas pequeno es",b)
elif (c<a and c<b and c<d and c<e):
     print ("El numero mas pequeno es",c)
elif (d<a and d<b and d<c and d<e):
    print ("El numero mas pequeno es",d)
else:
    print("El numero mas pequeno es",e)
    