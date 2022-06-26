#Escriba un programa que convierta de centímetros a pulgadas. 
#Una pulgada es igual a 2.54 centímetros.

while True:
    centimetros=input("Ingrese longitud: ")
    try:
        centimetros=float(centimetros)
        break
    except:
        pass

pulgadas=centimetros/2.54
print("{:.0f} cm = {:.4f} in".format(centimetros,pulgadas))
