#Escriba un programa que calcule el promedio 
#de 4 notas ingresadas por el usuario:

def solicitar_nota(texto):
    while True:
        nota=input(texto)
        try:
            nota=float(nota)
            return nota
        except:
            pass

nota1=solicitar_nota("Primera nota: ")
nota2=solicitar_nota("Segunda nota: ")
nota3=solicitar_nota("Tercera nota: ")
nota4=solicitar_nota("Cuarta nota: ")

promedio=(nota1+nota2+nota3+nota4)/4

print("El promedio es {:.2f}".format(promedio))
