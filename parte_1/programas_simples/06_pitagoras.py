#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b 
#de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c 
#del triangulo, dado por el teorema de Pitágoras: c²=a²+b².

import math

def solicitar_cateto(texto):
    while True:
        cateto=input(texto)
        try:
            cateto=float(cateto)
            if cateto>0:
                return cateto
            else:
                print("El tamaño del cateto no puede ser negativo")
        except:
            pass

cateto_a=solicitar_cateto("Ingrese cateto a: ")
cateto_b=solicitar_cateto("Ingrese cateto b: ")

hipotenusa=math.sqrt((math.pow(cateto_a,2)+math.pow(cateto_b,2)))

print(f"la hipotenusa es {hipotenusa}")