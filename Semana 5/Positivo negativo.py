#Numero positivo, negativo o cero
#ALGORITMO
#1. Pedir el número
#2. Mostrar número 
#3 Comparar si el numero es > que 0 
#4. Mostrar que el numero es positivo
#5. Si el numero es < que cero 
#6. Mostrar que el numero es negativo
#7. Si el numero es = a 0
#8. Mostrar que el numero es neutro

#PSEUDOCODIGO
#INICIO
    #ESCRIBIR "Ingrese el numero"
    #LEER numero
    #Si numero > que 0
    #ESCRIBIR "Numero positivo"
    #Si numero < que 0
    #ESCRIBIR "Numero negativo"
    #Sino 
    #ESCRIBIR "Numero neutro"
    #FinSi
#FIN 

numero=int(input("Ingrese numero: "))
if numero > 0:
  print ("El numero es positivo")
elif numero < 0:
  print ("El numero es negativo")
else: 
 print("El numero es cero")
