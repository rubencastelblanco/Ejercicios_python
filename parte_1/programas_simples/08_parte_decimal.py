#Escriba un programa que entregue la parte decimal 
#de un número real ingresado por el usuario.

import math

while True:
    numero=input("Ingrese un numero: ")

    #extrae la cantidad de decimales que tiene 
    if numero.count(".")>0:
        decimal_string=numero.split(".")[1]
        cantidad_decimales=len(decimal_string)
    else:
        cantidad_decimales=0

    #intenta volverlo un numero
    try:
        numero=float(numero)
        break
    except:
        pass

numero=math.fabs(numero)
entera=math.trunc(numero)
decimal=numero-float(entera)

#decimal,entera=math.modf(numero)
if cantidad_decimales==0:
    print(0)
else:
    print(round(decimal,cantidad_decimales))