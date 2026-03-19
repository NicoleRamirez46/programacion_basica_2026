#ALGORITMO
#1. computadora1 = "piedra"
#2. Pedir al usuario que ingrese su elección (piedra, papel o tijera)
#3. Leer la elección del usuario (eleccion)
#4. Comparar Si usuario = "piedra" y computadora1 = "piedra" Entonces
#5. Mostrar "Empate"       
#6. Comparar Si usuario = "piedra" y computadora1 = "tijera" Entonces
#7. Mostrar "Usuario gana"
#8. Comparar Si usuario = "tijera" y computadora1 = "papel" Entonces
#9. Mostrar "Usuario gana"
#10. Comparar Si usuario = "papel" y computadora1 = "piedra" Entonces
#11. Mostrar "Usuario gana"
#12. En cualquier otro caso 
#13. Mostrar "Computadora gana"
#14. Mostrar resultados

#PSEUDOCODIGO
#INICIO
    #computadora1 = "piedra"
    #ESCRIBIR "Ingrese su elección (piedra, papel o tijera): "
    #LEER eleccion
    #Si eleccion == "piedra" y computadora1 == "piedra" Entonces
        #ESCRIBIR "Empate"
    #Si eleccion == "piedra" y computadora1 == "tijera" Entonces
        #ESCRIBIR "Usuario gana"
    #Si eleccion == "tijera" y computadora1 == "papel" Entonces
        #ESCRIBIR "Usuario gana"
    #Si eleccion == "papel" y computadora1 == "piedra" Entonces
        #ESCRIBIR "Usuario gana"
    #En cualquier otro caso
        #ESCRIBIR "Computadora gana"
    #ESCRIBIR "La computadora eligió: ", computadora1
#FIN

computadora1 = "piedra"
print ("Bienvenido al juego de piedra, papel o tijera")
eleccion = input("Ingrese su elección (piedra, papel o tijera): ")
print ("La computadora eligió: ", computadora1)
if eleccion == "piedra" and computadora1 == "piedra":
    print ("Empate, porque ambos eligieron piedra")
elif eleccion == "piedra" and computadora1 == "tijera":
    print ("Ganaste , porque piedra aplasta tijera")
elif eleccion == "tijera" and computadora1 == "papel":
    print ("Ganaste, porque tijera corta papel")
elif eleccion == "papel" and computadora1 == "piedra":  
    print ("Ganaste, porque papel envuelve piedra")
elif eleccion != "piedra" and eleccion != "papel" and eleccion != "tijera":
    print ("Elección inválida, por favor ingrese piedra, papel o tijera")
else:
    print ("Computadora gana, porque ", computadora1, " gana a ", eleccion)

print ("Gracias por jugar, ¡hasta la próxima!")
