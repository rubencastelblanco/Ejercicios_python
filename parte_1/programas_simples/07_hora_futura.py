#Escriba un programa que pregunte al usuario la hora actual t del reloj 
#y un número entero de horas h, 
#que indique qué hora marcará el reloj dentro de h horas:

def solicitar_hora(texto):
    while True:
        hora=input(texto)
        try:
            hora=int(hora)
            if hora>0:
                return hora
        except:
            pass

hora_actual=solicitar_hora("Hora actual: ")
sumar_horas=solicitar_hora("Cantidad de horas: ")
hora_futura=hora_actual+sumar_horas

while hora_futura>=24:
    hora_futura-=24

print(f"En {sumar_horas} horas, el reloj marcara las {hora_futura} ")