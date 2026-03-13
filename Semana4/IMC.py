#ALGORITMO
#1. Pedir el nombre del usuario
#2. Pedir el peso en kilogramos al usuario
#3. Pedir la altura en metros al usuario
#4. Calcular el IMC(Indice de Masa Corporal) = Peso/(altura*altura)
#5. Mostrar el peso
#6. Mostrar la altura
#7. Mostrar el IMC
#8. Comparar si el rango del IMC esta dentro del rango normal >= 18.5 o <=24.9
#9. Mostrar el resultado True o False 

#PSEUDOCODIGO
#INICIO
    #LEER Nombre
    #LEER Peso
    #LEER Altura
    #IMC <-Peso/(Altura*Altura)
    #Rangonormal<- IMC >= 18.5 Y IMC <= 24.9
    #ESCRIBIR "Nombre: ", Nombre
    #ESCRIBIR "Peso (kg): ", Peso
    #ESCRIBIR "Altura (m): ", Altura
    #ESCRIBIR "IMC (Indice de Masa Corporal): ", IMC
    #ESCRIBIR "¿La persona esta en el rango normal?: ", Rangonormal
#FIN
Nombre =input("Ingrese su nombre: ")
Peso = float(input("Ingrese su peso(kg): "))
Altura = float (input("Ingrese su altura(m): "))
print ("El rango normal esta entre 18.5 y 24.9")

IMC = Peso/(Altura*Altura)
RangoNormal = IMC >= 18.5 and IMC <= 24.9

print("Nombre: ", Nombre)
print("Peso: ", Peso)
print("Altura: ", Altura)
print("IMC (Indice de Masa Corporal): ", IMC)
print("¿La persona esta en el rango normal?: ", RangoNormal)
