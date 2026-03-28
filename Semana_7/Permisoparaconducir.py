edad=int(input("Ingresa tu edad: "))
tienelicencia = input("¿Tienes licencia vigente?(si/no):")

if edad >=18  and tienelicencia == "si":
    print ("Puedes conducir.¡Maneja con cuidado!")
else:
    print ("No puedes conducir.")
