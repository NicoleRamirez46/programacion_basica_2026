#ALGORITMO 
#1. Pedir el nombre al usuario
#2. Pedir la edad del usuario
#3. Pedir la ciudad del usuario
#4. Mostrar el nombre 
#5. Mostrar la edad
#6. Mostrar la ciudad
#7. Comparar si la edad es mayor o igual a 18
#8. Mostrar el resultado True o False

#PSEUDOCODIGO 
#INICIO 
    #LEER nombre
    #LEER edad
    #LEER ciudad
    #ESCRIBIR "Hola, me llamo", nombre
    #ESCRIBIR "Tengo", edad, "años"
    #ESCRIBIR "Soy de", ciudad 
    #ESCRIBIR "Es mayor de edad", edad>18
#FIN

Name = input("Escribe tu nombre: ")
Age = int (input("Escribe tu edad: "))
City = input("¿Donde vives?: ")
print("Hola, me llamo", Name)
print("Tengo ", Age, "años")
print("Soy de ", City)
print("¿Eres mayor de edad?", Age>18)
