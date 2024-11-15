#
# Programa que muestra los años bisiestos entre dos años dados.
#

inicio = 1700
fin = 2100

# Condiciones para que un año bisesto:
# - Es divisible por 4
# - No es divisible por 100, a menos que sea divisible por 400

for ano in range(inicio, fin+1):
    if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
        print(ano, end="\t")

