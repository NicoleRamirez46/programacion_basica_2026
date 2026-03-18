#ALGORITMO
#1. Pedir el color
#2. Mostrar color
#3 Comparar si el color es Verde 
#4. Mostrar que puede continuar
#5. Si el color es Amarillo
#6. Mostrar que debe tener precaución
#7. Si el color es Rojo
#8. Mostrar que debe detenerse

#PSEUDOCODIGO
#INICIO
    #ESCRIBIR "Ingrese el color"
    #LEER color
    #Si color es Verde
    #ESCRIBIR "Puede continuar"
    #Si color es Amarillo
    #ESCRIBIR "Tenga precaución"
    #Si color es Rojo
    #ESCRIBIR "Debe detenerse"
    #FinSi
#FIN 

semaforo=input("Dame el color del semaforo: ")
if semaforo=="rojo":
 print ("Debe detenerse")
elif semaforo=="amarillo":
  print ("Tenga precaucion")
elif semaforo=="verde":
  print ("Puede continuar")
