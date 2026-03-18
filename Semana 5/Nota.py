#ALGORITMO
#Pedir al usuario la nota final
#Leer la nota
#Si la nota es >= a 3.0
#Mostrar Apruebas la materia, felicidades
#Sino 
#Mostrar Reprobaste la materia. Debes presentar la recuperación

#PSEUDOCODIGO
#INICIO
        #ESCRIBIR "Ingrese la nota final: "
        #LEER nota
        #Si nota >=3.0 Entonces
        #ESCRIBIR "Aprobaste la materia, felicidades."
        #Sino
        #ESCRIBIR "Reprobaste la materia. Debes presentar la recuperación"
#FIN

nota=float(input("Digite su nota "))
if nota >= 3.0: 
    print ("Apruebas la materia, ¡Felicitaciones! :D")
else:
  print('Reprobaste la materia. Debes presentar la recuperación :(')
