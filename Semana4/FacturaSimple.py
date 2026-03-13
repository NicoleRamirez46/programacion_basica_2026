#ALGORITMO 
#1. Pedir el nombre del producto al usuario
#2. Pedir el precio por unidad del producto al usuario
#3. Pedir la cantidad del producto
#4. Calcular el precio (Precio* Cantidad)
#5. Calcular el IVA (Subtotal*0.19)
#6. Calcular el total (Subtotal + IVA)
#7. Mostrar el precio
#8. Mostrar el IVA
#9. Mostrar el total a pagar
#10. Comparar si el total >= 50000 para aplicar el descuento
#11. Mostrar el resultado True o False

#PSEUDOCODIGO
#INICIO 
    #LEER Nombreproducto
    #LEER Preciounidad
    #LEER Cantidad
    #Subtotal <- Preciounidad *Cantidad
    #IVA<-Subtotal*0.19
    #Total<-Subtotal + IVA
    #ESCRIBIR "Subtotal: ", Subtotal
    #ESCRIBIR "IVA: ", IVA
    #ESCRIBIR "El total a pagar es: ", Total
    #ESCRIBIR "¿El cliente tiene descuento?: ", Total >=50000
#FIN

Producto = input("Ingrese el nombre del producto: ")
Precio = float(input("Ingrese el precio por unidad: "))
Cantidad = int(input("Ingrese la cantidad: "))

Subtotal = Precio * Cantidad
IVA = Subtotal * 0.19
Total = Subtotal + IVA 

print ("Producto: ", Producto)
print ("Precio por unidad: ", Precio)
print ("Cantidad: ", Cantidad)
print ("Subtotal: ", Subtotal)
print ("IVA (19%): ", IVA)
print ("Total a pagar: ", Total)

print ("¿El cliente tiene descuento?: ", Total >= 50000)
