# calculadoraMultiplicacion.py

def multiplicacion(a, b):
    return a * b

def main():
    print("Calculadora de Multiplicación:")
    print("3. Multiplicación")

    opcion = int(input("Elige una operación (3 para Multiplicación): "))

    # Solo permite continuar si se selecciona la opción 3
    if opcion == 3:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", multiplicacion(a, b))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
