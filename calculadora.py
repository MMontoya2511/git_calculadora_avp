# calculadoraResta.py

def resta(a, b):
    return a - b

def main():
    print("Calculadora de Resta:")
    print("1. Resta")

    opcion = int(input("Elige una operación (2 para Resta): "))

    # Solo permite continuar si se selecciona la opción 1
    if opcion == 2:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", resta(a, b))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()


