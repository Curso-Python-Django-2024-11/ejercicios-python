#!/usr/bin/env python3
# Programa para obtener estadísticas de datos numéricos

# 1. Toma de datos
datos = input("Introduzca los datos separados por espacios: ")
muestras = [float(x) for x in datos.split()]

# 2. Cálculo de estadísticas
numero_muestras = len(muestras)
suma = sum(muestras)
media = suma / numero_muestras
maximo = max(muestras)
minimo = min(muestras)
varianza = sum((x - media) ** 2 for x in muestras) / numero_muestras
desviacion_tipica = varianza ** 0.5

# 3. Presentación de resultados
# https://docs.python.org/es/3.13/library/string.html#format-specification-mini-language
print("Número de muestras:", numero_muestras)
print("Suma:", suma)
print(f"Media: {media:.4f}")
print("Máximo:", maximo)
print("Mínimo:", minimo)
print("Varianza:", varianza)
print("Desviación típica:", desviacion_tipica)