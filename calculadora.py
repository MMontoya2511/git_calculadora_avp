# calculadora.py

def suma(a, b):
    return a + b

def main():
    print("Calculadora de Suma:")
    print("1. Suma")

    opcion = int(input("Elige una operación (1 para Suma): "))

    # Solo permite continuar si se selecciona la opción 1
    if opcion == 1:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", suma(a, b))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()

