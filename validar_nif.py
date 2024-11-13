# Introducción del NIF
nif = input("Introduce tu NIF: ")
LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"

# Limpieza del string
nif = nif.strip().upper()

# Separación de numero y letra
numero = int(nif[:-1])
letra = nif[-1]

# Cálculo de la letra y comprobación final
resto = numero % 23
if letra == LETRAS[resto]:
    print("El NIF es correcto")
else:
    print("El NIF es incorrecto")