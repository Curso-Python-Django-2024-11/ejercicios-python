# Indice de Masa Corporal (IMC)

# 1. Pedir al usuario su peso en kg y su estatura en metros
print("Calculadora de IMC")
peso = float(input("Introduzca su peso en kg: "))
estatura = float(input("Introduzca si altura en m: "))

# 2. Cálculo del IMC
imc = peso / estatura ** 2

# 3. Mostrar el resultado
print("Su IMC es:", round(imc, 2))