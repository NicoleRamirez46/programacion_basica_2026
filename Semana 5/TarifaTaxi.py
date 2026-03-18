#ALGORITMO
#1. Mostrar un mensaje de bienvenida al usuario
#2. Mostrar la tarifa base del servicio de taxi
#3. Pedir al usuario la distancia del viaje en kilometros (km)
#4. Leer el valor de la distancia (distancia)
#5. Pedir La hora del viaje (hora)
#6. Leer el valor de la hora (hora)
#7. Iniciar total = tarifa base
#8. Si la distancia es > 10 km Entonces
#9. Calcular el costo adicional por km (distancia - 10)
#10. Calcular el costo extra = km adicional*800 
#11. Sumar <-costo extra + total
#12. Si la hora esta entre las 21 y las 5 Entonces
#13. Calcular el recargo nocturno = total*0.3
#14. Sumar <- recargo nocturno + total
#15. Mostrar el total a pagar por el servicio de taxi

#PSEUDOCODIGO
#INICIO
    #ESCRIBIR "Bienvenido al servicio de taxi"
    #tarifabase = 5000
    #ESCRIBIR "La tarifa base del servicio de taxi es: ", tarifabase
    #ESCRIBIR "Ingrese la distancia del viaje en kilometros (km): "
    #LEER distancia
    #ESCRIBIR "Ingrese la hora del viaje (hora): "
    #LEER hora
    # total = tarifabase
    #Si distancia > 10 Entonces
    #km adicional = distancia - 10
    #costo extra = km adicional*800
    #total = costo extra + total
    #Si hora > 21 o hora < 5 Entonces
    #recargo nocturno = total*0.3
    #total = recargo nocturno + total
    #ESCRIBIR "El total a pagar por el servicio de taxi es: ", total
#FIN           

print ("Bienvenido al servicio de taxi")
TarifaBase = 5000
print ("La tarifa base del servicio de taxi es: ", TarifaBase)
Distancia = float(input("Ingrese la distancia del viaje en kilometros (km): "))
Hora =int(input("Ingrese la hora del viaje (hora): "))
Total = TarifaBase
if Distancia > 10:
    KmAdicional = Distancia - 10
    CostoExtra = KmAdicional*800
    Total = CostoExtra + Total
if Hora >=21 or Hora < 5:
    RecargoNocturno = Total*0.3
    Total = RecargoNocturno + Total 
print ("El total a pagar por el servicio de taxi es: ", Total)
print ("Gracias por usar nuestro servicio de taxi")
