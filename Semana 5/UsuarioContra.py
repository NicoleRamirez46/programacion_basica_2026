#ALGORITMO
#1. USUARIO CORRECTO = "admin"
#2. CONTRASEÑA CORRECTA = "uniminuto2024"
#3. Pedir al usuario que ingrese su nombre de usuario
#4. Pedir al usuario que ingrese su contraseña  
#5. Leer el nombre de usuario (usuario) y la contraseña (contraseña)
#6. Si el nombre de usuario es igual a USUARIO CORRECTO y la contraseña es igual a CONTRASEÑA CORRECTA Entonces
#7. Mostrar "Acceso concedido"
#8. Sino
#9. Mostrar "Acceso denegado"
#10. Repetir hasta tres veces

#PSEUDOCODIGO
#INICIO
    #USUARIO CORRECTO = "admin"
    #CONTRASEÑA CORRECTA = "uniminuto2024"
    #REPETIR 3 VECES
        #ESCRIBIR "Ingrese su nombre de usuario: "
        #LEER usuario
        #ESCRIBIR "Ingrese su contraseña: "
        #LEER contraseña
        #Si usuario == USUARIO CORRECTO y contraseña == CONTRASEÑA CORRECTA Entonces
            #ESCRIBIR "Acceso concedido"
        #Si usuario == USUARIO CORRECTO y contraseña != CONTRASEÑA CORRECTA Entonces
            #ESCRIBIR "Contraseña incorrecta, intente nuevamente."
        #Si usuario != USUARIO CORRECTO Entonces
            #ESCRIBIR "Usuario no encontrado, intente nuevamente."
    #FinREPETIR
    #FinSi
#FIN

USUARIOCORRECTO = "admin"
CONTRASEÑACORRECTA = "uniminuto2024"
print ("Bienvenido al sistema de acceso de la universidad")
usuario = input("Ingrese su nombre de usuario: ")
contraseña = input("Ingrese su contraseña: ")
intentos =0
if usuario == USUARIOCORRECTO and contraseña == CONTRASEÑACORRECTA:
        print ("Acceso concedido")
elif usuario == USUARIOCORRECTO and contraseña != CONTRASEÑACORRECTA:
        print ("Contraseña incorrecta, intente nuevamente.")
else: 
    usuario != USUARIOCORRECTO
    print ("Usuario no encontrado, intente nuevamente.")
