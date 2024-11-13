import random

TAM_PASSWORD = 8
CARACTERES = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+@#$%&/()="
l = random.choices(CARACTERES, k=TAM_PASSWORD)

# Transformar la lista l en una string, uniendo todos sus elementos
password = "".join(l)

# Mostrar la contraseña generada
print("Password generada", password)