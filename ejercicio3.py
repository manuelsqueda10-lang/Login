
#login
USUARIO_ADMIN = "Administrador"
CONTRASENA = "12345"

Usuario_privilegiado = input("Ingresa tu usuario: ")
Contrasenia = input("Ingresa contrasenia: ")  # sin int()

if USUARIO_ADMIN == Usuario_privilegiado and CONTRASENA == Contrasenia:
    print("Bienvenido")
else:
    print("ERROR")