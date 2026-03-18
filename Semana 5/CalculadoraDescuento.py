#ALGORITMO
#1. Pedir el valor de la compra
#2. Leer el valor
#3. Si el valor es >100000
#4. Calcular si tiene Descuento= valor*0.15
#5. Calcular el Total a pagar= valor-Descuento
#6. Mostrar Felicitaciones obtuviste un descuento
#7. Sino
#8. El total a pagar es igual al valor de la compra
#9. Mostrar no obtuviste descuento, 
#8. El valor de la compra es: 

#PSEUDOCODIGO
#INICIO 
    #ESCRIBIR "Ingrese el valor de la compra: "
    #LEER valor
    #Si valor >100000 Entonces
    #Descuento <- valor*0.15
    #Total <- valor - Descuento
    #ESCRIBIR "Felicitaciones obtuviste un descuento :D
    #Sino 
    #Total= valor
    #ESCRIBIR "No obtuviste descuento :()"
    #FinSi
    #ESCRIBIR "El valor de la compra es:"

valor=int(input("Ingrese el valor de la compra: "))
valor 
if valor > 100000:
    Descuento = valor * 0.15 
    Total = valor - Descuento
    print ("Felicitaciones obtuviste un descuento :D")
    print ("El valor de la compra es: ", Total)
else: 
    Total = valor
    print ("No obtuviste el descuento, sigue intentando :( ")
    print ("El valor de la compra es: ", Total)
