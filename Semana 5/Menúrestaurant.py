#ALGORITMO
#1. Mostrar el menú del restaurante
#2. Pedir al usuario que elija una opción del menú
#3. Leer la opción que el usuario ha elegido
#4. Si la opción es 1 mostrar el plato del día y el precio
#5. Si la opción es 2, mostrar el plato del dia y el precio
#6. Si la opción es 3, mostrar el plato del dia y el precio
#7. Si no es ninguna de las opciones anteriores, mostrar un mensaje de error indicando que la opción no es válida.

#PSEUDOCODIGO
#INICIO
    #ESCRIBIR "Bienvenido al restaurante la mariposa"
    #ESCRIBIR "Nuestro menú del día es: "
    #ESCRIBIR "1. Bandeja paisa, precio: 18000"
    #ESCRIBIR "2. Ajiaco, precio: 15000"
    #ESCRIBIR "3. Sancocho, precio: 12000"
    #ESCRIBIR "Por favor elija una opción del menú: "
    #LEER opcion
    #Si opcion = 1 Entonces
    #ESCRIBIR "Elegiste: Bandeja paisa, precio: 18000"
    #Sino 
    #Si opcion = 2 Entonces
    #ESCRIBIR "Elegiste: Ajiaco, precio: 15000"
    #Sino
    #Si opcion = 3 Entonces             
    #ESCRIBIR "Elegiste: Sancocho, precio: 12000"
    #Sino
    #ESCRIBIR "Opción no válida, por favor elija una opción del menú"   
#FIN

print ("Bienvenido al restaurante la Mariposa")
print ("Nuestro menú del dia es:")
print ("1. Bandeja paisa") 
print ("2. Ajiaco") 
print ("3. Sancocho")
opcion = int(input("Por favor elija una opción del menú: "))

if opcion == 1:
    print ("Elegiste: Bandeja paisa, precio: 18000")
elif opcion == 2:
    print ("Elegiste: Ajiaco, precio: 15000")
elif opcion == 3:
    print ("Elegiste: Sancocho, precio: 12000")
else:
    print ("Opción no válida, por favor elija una opción del menú")
