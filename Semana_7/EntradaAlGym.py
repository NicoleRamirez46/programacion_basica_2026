#PSEUDOCODIGO
#INICIO
#PARTE A
  #ESCRIBIR "Ingrese su edad"
  #LEER a
  #ESCRIBIR "¿Tiene carnet de socio vigente? (si/no)"
  #LEER b
  #Si edad >14 Y tiene carnet == "si" ENTONCES
  #ESCRIBIR "Bienvenido al gimnasio"
  #Sino
  #ESCRIBIR "Acceso denegado"
#FIN

#PARTE B
  #ESCRIBIR "¿Tienes pase de invitado? (si/no)"
  #LEER c
  #ESCRIBIR "¿Viene con socio? (si/no)"
  #LEER d
 #Si c == "si" O d == "si" ENTONCES
  #ESCRIBIR "Puede ingresar al Gym :D"
  #SINO
  #ESCRIBIR "No puede ingresar al Gym :c")
#FIN
#PARTE A
a = int(input("Ingrese su edad: "))
b = input("¿Tiene carnet de socio vigente? (si/no): ")
if a > 14 and b == "si":
  print("Bienvenido al gimnasio")
else:
  print("Acceso denegado")

#PARTE B
c = input("¿Tiene pase de invitado? (si/no): ")
d = input("¿Viene con socio activo?: ")
if c == "si" or d == "si":
  print("Puede ingresar al Gym :D")
else:
  print("No puede ingresar al Gym :c")
