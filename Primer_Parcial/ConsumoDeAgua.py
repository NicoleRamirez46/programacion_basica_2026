#ALGORITMO
#Pedir al usuario el nombre
#Mostrar el nombre del usuario 
#Pedir al usuario que ingrese el consumo mensual de agua en metros cubicos 
#Mostrar el consumo mensual de agua del usuario
#Comparar si el consumo es >= 1 y <= 15 metros cubicos Entonces
#Mostrar ¡Excelente! Eres un usuario responsable del agua.
#Si el consumo es >= 16 <= 30 metros cubicos Entonces
#Mostrar Tu consumo esta dentro del promedio del hogar
#Si el consumo es >= 30 metros cubicos Entonces 
#Mostrar ATENCION: Tu consumo es alto, revisa posibles fugas
#Si el consumo es <=0 Entonces
#Mostrar Error: el consumo debe ser mayor a 0 

nombre=input("Ingrese su nombre: ")
consumo=int(input("Ingrese el consumo mensual de agua: "))
print("El consumo mensual de agua es: ",consumo)
if consumo >= 1 and consumo <=15:
    print("¡Excelente! Eres un usuario responsable del agua.")
elif consumo>=16 and consumo<=30:
    print("Tu consumo esta dentro del promedio del hogar")
elif consumo>=30:
    print("ATENCION: Tu consumo es alto, revisa posibles fugas")
elif consumo<=0:
    print("Error: el consumo debe ser mayor a 0")
