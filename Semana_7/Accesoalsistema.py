USUARIOCORRECTO= "admin"
CONTRASEÑACORRECTA= 1234
usuario= input ("Escribe el nombre de usuario: ")
contraseña= int(input("Escribe tu contraseña: "))
if usuario == USUARIOCORRECTO and contraseña == CONTRASEÑACORRECTA:
    print ("Acceso concedido. ¡Bienvenido!")
    print ("Cargando tu perfil...")
else:
    print ("Acceso denegado. Datos incorrectos.")
