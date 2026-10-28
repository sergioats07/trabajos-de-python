import random
import string
long = int(input("¿De cuántos caracteres quieres tu contraseña? "))
def generar_password(saka):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(caracteres) for _ in range(saka))
    return password


print(f"Tu contraseña generada es: {generar_password(long)}")



