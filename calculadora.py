
# calculadora.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def main():
    print("Calculadora:")
    print("1. Suma")
    print("2. Resta")

    opcion = int(input("Elige una operación (1 para Suma, 2 para Resta): "))

    if opcion == 1:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la suma:", suma(a, b))
    elif opcion == 2:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la resta:", resta(a, b))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
