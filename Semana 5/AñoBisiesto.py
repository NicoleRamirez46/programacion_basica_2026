#ALGORITMO
#1. Pedir al usuario el año a evaluar
#2. Leer el valor del año (año)
#3. Si el año es divisible por 4 Entonces
#4. Es bisiesto
#5. Si es divisible por 400 Entonces 
#6. Es bisiesto
#7. Sino cumple ninguna de las condiciones anteriores
#8. No es bisiesto
#9. Mostrar el resultado al usuario

#PSEUDOCODIGO
#INICIO
    #ESCRIBIR "Ingrese el año a evaluar; "
    #LEER año
    #Si año es divisible por 4 Entonces
    #ESCRIBIR "El año es bisiesto"
    #Si año es divisible por 400 Entonces
    #ESCRIBIR "El año es bisiesto"
    #Sino
    #ESCRIBIR "El año no es bisiesto"
#FIN

print ("Bienvenido al verificador de años bisiesto")
año=int(input("Ingrese el año a evaluar: "))
if año % 4 == 0:
    print ("El año es bisiesto")
elif año % 400 == 0:
    print ("El año es bisiesto")         
else:
    print ("El año no es bisiesto")
