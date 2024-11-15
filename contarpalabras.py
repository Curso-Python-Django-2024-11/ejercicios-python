contador = 0

with open("documento.txt", "r") as f:
    for linea in f:
        contador += len(linea.strip().split())

print(f"El documento contiene {contador} palabras.")