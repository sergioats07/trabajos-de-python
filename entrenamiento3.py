usuarios = {
    "iperurena": {
        "nombre": "iñaki",
        "apellido": "perurena",
        "contraseña": 12345,
    },
    "fmguruza": {
        "nombre": "fermin",
        "apellido": "muguruza",
        "contraseña": 54321,
    },

    "aolaizola":{
        "nombre":"aimar",
        "apellido":"olaizola",
        "contraseña": 21435
    }
}
intentos=3

while intentos>0:
    usuario=input("ingrese su nombre de usuario:")
    if usuario in usuarios:
        clave=int(input("ingrese su contraseña:"))
        if clave==usuarios[usuario]["contraseña"]:
            print("bienvenido",usuarios[usuario]["nombre"],usuarios[usuario]["apellido"])
            break
        else:
            intentos-=1
            print("contraseña incorrecta. le quedan", intentos, "intentos.")
    else:
        intentos-=1
        print("usuario no encontrado, quedan", intentos, "oportunidades.")

        
else:
    print("ha agotado todos sus intentos.")