#ALGORITMO
#1. Pedir el Num 1 al usuario
#2. Pedir el Num 2 al usuario
#3. Mostrar la Suma de Num 1 y Num 2
#4. Mostrar la Resta Num 1 y Num 2
#5. Mostrar la Multiplicación Num 1 y Num 2
#6. Mostrar la Division Num 1 y Num 2
#7. Mostrar la Division entera de Num 1 y Num 2
#8. Mostrar el Residuo de Num 1 y Num 2
#9. Mostrar la Potencia de Num 1 y Num 2
#10.Comparar si la suma es mayor a 100
#11. Mostrar el resultado True o False

#PSEUDOCODIGO 
#INICIO 
    #LEER Num1
    #LEER Num2
    #Suma <- Num1 + Num2
    #Resta <- Num1 - Num2
    #Multiplicacion <- Num1 * Num2
    #Division <- Num1 / Num2
    #Division Entera<-Num1 // Num2
    #Residuo <- Num1 % Num2
    #Potencia<-Num1 ** Num2

    #ESCRIBIR "Suma: ", Suma
    #ESCRIBIR "Resta: ", Resta
    #ESCRIBIR "Multiplicacion: ", Multiplicacion
    #ESCRIBIR "Division: ", Division
    #ESCRIBIR "Division Entera: ", Division Entera
    #ESCRIBIR "Residuo: ", Residuo
    #ESCRIBIR "Potencia: ", Potencia
    #ESCRIBIR "¿La suma es mayor a 100?: ", Suma>100
#FIN

Num1 = int(input("Ingrese el primer número entero: "))
Num2 = int(input("Ingrese el segundo número entero: "))

print("La suma es: ", Num1+Num2)
print("La resta es: ", Num1-Num2)
print("La multiplicación es: ", Num1*Num2)
print("La división es: ", Num1/Num2)
print("La división entera es: ", Num1//Num2)
print("El residuo es: ",Num1%Num2)
print("La potencia es: ", Num1**Num2)

print("¿La suma es mayor que 100: ", Num1+Num2>100)
