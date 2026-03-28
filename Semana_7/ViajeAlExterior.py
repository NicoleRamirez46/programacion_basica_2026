Pasaporte= input("¿Tienes pasaporte vigente?(si/no): ")
Visa= input("Tienes visa (si/no): ")
Exento= input("Tu país esta exento de Visa: ")

if Pasaporte == "si" and (Visa == "si" or Exento == "si"): 
    print ("Puedes viajar. !Buen viaje :D¡")
else:
    print ("No puedes viajar. Revisa tus documentos :c")
