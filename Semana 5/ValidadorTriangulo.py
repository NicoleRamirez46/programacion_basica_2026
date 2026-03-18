#ALGORITMO
#1. Pedir los tres lados del triangulo
#2. Leer los valores (lado1,lado2,lado3)
#3. Verificar si cumplen la desigualdad triangular
#4. Si lado1 + lado2 > lado3 
#5. Si lado1 + lado3 > lado2
#6. Si lado2 + lado3 > lado1
#7. Si sí se cumple
#8. Si lado1 == lado2 == lado3 Entonces
#9. Mostrar El triangulo es equilatero
#10. Si lado1 == lado2 o lado1 == lado3 o lado2 == lado3 Entonces
#11. Mostrar El triangulo es isosceles
#12. Si lado1 != lado2 != lado3 Entonces    
#13. Mostrar El triangulo es escaleno
#14. Sino
#15. Mostrar Los lados ingresados no forman un triangulo


#PSEUDOCODIGO
#INICIO
    #ESCRIBIR "Ingrese el valor del lado 1: "
    #LEER lado1
    #ESCRIBIR "Ingrese el valor del lado 2: "
    #LEER lado2
    #ESCRIBIR "Ingrese el valor del lado 3: "
    #LEER lado3
    #Si lado1 + lado2 > lado3 
    #Si lado1 + lado3 > lado2 
    #Si lado2 + lado3 > lado1 
    #Si se cumple Entonces
    #Si lado1 == lado2 == lado3 Entonces
    #ESCRIBIR "El triangulo es equilatero"
    #Sino 
    #Si lado1 == lado2 o lado1 == lado3 o lado2 == lado3 Entonces
    #ESCRIBIR "El triangulo es isosceles"
    #Sino
    #Si lado1 != lado2 != lado3 Entonces    
    #ESCRIBIR "El triangulo es escaleno"
    #Sino
    #ESCRIBIR "Los lados ingresados no forman un triangulo"
    #FinSi
#FIN

print ("Bienvenido al validador de triangulos")
lado1 = float(input("Ingrese el valor del lado 1: "))
lado2 =float(input("Ingrese el valor del lado 2: "))
lado3 = float(input("Ingrese el valor del lado 3: "))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
  if lado1 == lado2 == lado3:
        print ("El triangulo es equilatero")
  elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print ("El triangulo es isosceles")
  else: 
        print ("El triangulo es escaleno")
  else:
    print ("Los lados ingresados no forman un triangulo")
