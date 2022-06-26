#Escriba un programa que reciba como entrada el radio de un círculo
#y entregue como salida su perímetro y su área 
#perimetro=2*pi*radio, area=pi*r²

#-------------------solucion---------------
import math

while True:
    radio=input("Ingrese el radio: ")
    try:
        radio=float(radio)
        break
    except:
        pass

perimetro=2*math.pi*radio
area=math.pi*math.pow(radio,2)

print("Perimetro: {:.1f}".format(perimetro))
print("Area: {:.1f}".format(area))