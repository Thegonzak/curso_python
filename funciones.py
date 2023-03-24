print("Aqui comienza el codigo del programa")

# COMENTARIOS

ARS: float = 202.91
COL: float = 4849.99
MEX: float = 18.74

nombre = input("Ingrese nombre:")
print(f"Hola {nombre} bienvenidos al conversor de monedas")

print("1 - Dolares estaunidenses a pesos agentinos")
print("2 - Dolares estaunidenses a pesos colombianes")
print("3 - Dolares estaunidenses a pesos mexicanos")

opcion = int(input("Cual es la opción: "))


def conversion(num: float) -> float:
    dolares = int(input("Cuantos dolares tienes: "))
    pesos: float = num * dolares
    return pesos


if opcion == 1:
    print(f"Tienes {conversion(ARS)} pesos argentinos")

elif opcion == 2:
    print(f"Tienes {conversion(COL)} pesos colombianos")

elif opcion == 3:
    print(f"Tienes {conversion(MEX)} pesos mexicanos")

elif opcion != 1 or opcion != 2 or opcion != 3:
    print(f"EL valor ingresado no es el correcto")
