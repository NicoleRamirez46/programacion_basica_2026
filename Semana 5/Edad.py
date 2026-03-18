#ALGORITMO
#1. El usuario ingresa la edad
#2. Mostrar la edad
#3. Comparar si la edad es >=18
#4. Mostrar Puede ingresar a la discoteca
#5. Si no
#6. Mostrar "No puede ingresar a la discoteca"_

#PSEUDOCODIGO
#INICIO
  #ESCRIBIR "Ingrese su edad: "
  #LEER edad
  #Si edad es >= 18 Entonces
  #Escribir "Puede ingresar a la discoteca"
  #Sino
  #Escribir "No puede ingresar a la discoteca"
  #FinSi
#FIN

edad=int(input("Ingrese su edad "))
if edad >= 18:
 print("Puedes entrar al a distoteca")
else:
  print('Vayase para su casa')
