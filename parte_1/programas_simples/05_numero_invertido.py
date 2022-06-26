#Escriba un programa que pida al usuario un entero de tres dígitos, 
#y entregue el número con los dígitos en orden inverso:

while True:
    numero=input("Ingrese numero: ")
    try:
        if numero.isdigit() and len(numero)==3:
            invertido=numero[::-1]
            break
        else:
            print("Error: escribe un numero de 3 digitos")
    except:
        pass

print(invertido)