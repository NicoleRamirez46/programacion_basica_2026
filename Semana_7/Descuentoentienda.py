Es_estudiante= input("¿Eres estudiante? (si/no): ")
Total= int(input("Ingrese el valor de tu compra: "))
 
if Es_estudiante == "si" or Total> 200000:
    descuento= Total*0.15
    Total_final= Total-descuento 
    print ("¡Obtuviste un descuento del 15%!")
    print ("Descuento: ", descuento)
    print ("Total a pagar: ",Total_final)
else: 
    print ("Sin descuento. Total a pagar:", Total)
