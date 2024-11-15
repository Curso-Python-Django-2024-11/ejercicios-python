# Ecuaciones de segundo grado
# Ecuaiones de la forma ax^2 + bx + c = 0
# Obtiene las soluciones reales de este tipo de ecuaciones
from math import sqrt

# Solicitar datos
print("Ecuación ax^2 + bx + c = 0")
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

# Calcular el discriminante
d = b**2 - 4*a*c

if d >= 0:
    # Calcular las dos soluciones
    x1 = (-b + sqrt(d)) / (2*a)
    x2 = (-b - sqrt(d)) / (2*a)

    # Mostrar resultados
    print(f"Las soluciones son: {x1:.4f} y {x2:.4f}")
else:
    print("Esta ecuación no tiene soluciones reales")
    