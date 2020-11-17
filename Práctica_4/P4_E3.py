# Practica 4
# Ejercicio 3
# Pida al usuario si quiere calcular el area de un triangulo o un cuadrado,\
# y pida los datos segun que caso y muestre el resultado.

respuesta=input("Hola, bienvenido al calculador de areas, que area deseas \
calcular Cuadrado o Triangulo. ")
if (respuesta=="Triangulo"):
    base=float(input("Indica la base del trinagulo. "))
    altura=float(input("Indica la altura del triangulo. "))
    area_triangulo=(base*altura/2)
    print ("El area del triangulo es igual a ",area_triangulo)
elif (respuesta=="Cuadrado"):
    lado=float(input("Introduzca el lado del cuadrado. " ))
    area_cuadrado=(lado*lado)
    print("El area del cuadrado es ",area_cuadrado)
else:
    print("No has indicado una respuesta valida.")
    

