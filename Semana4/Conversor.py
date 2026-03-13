#ALGORITMO 
#1. Pedir la temperatura en grados Celsius
#2. Mostrar (Celsius *9/5) + 32
#3. Mostrar la temperatura en grados Fahrenheit
#4. Mostrar Celsius + 273.15
#5. Mostrar la temperatura en grados Kelvin
#6. Comparar si la temperatura en grados Celsius supera los 37 grados
#7. Mostrar el resultado True o False

#PSEUDOCODIGO 
#INICIO 
    #LEER Celsius
    #Fahrenheit <- (Celsius * 9/5) + 32
    #Kelvin <- Celsius + 273.15
    #ESCRIBIR "La temperatura en grados Celsius es:", Celsius
    #ESCRIBIR "La temperatura en grados Fahrenheit es: ", Fahrenheit
    #ESCRIBIR "La temperatura en grados Kelvin es: ", Kelvin
    #ESCRIBIR "¿La temperatura es supera los 37 grados?: ", Celsius > 37
#FIN

print ("BIENVENIDO AL CONVERSOR DE TEMPERATURA")
Celsius= float(input("Ingrese la temperatura en grados Celsius: "))
Fahrenheit= (Celsius *9/5) + 32
Kelvin = Celsius + 273.15
print("La temperatura en grados Celsius es: ", Celsius)
print("La temperatura en grados Fahrenheit es: ", Fahrenheit)
print("La temperatura en grados Kelvin es: ", Kelvin)
print("¿La temperatura es supera los 37 grados?: ", Celsius>37)
