# calculadora.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero."
    return a / b

def main():
    print("Calculadora básica:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = int(input("Elige una operación (1/2/3/4): "))

    # Asegurarnos de que solo muestra los mensajes cuando la opción es válida
    if opcion in [1, 2, 3, 4]:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))

        if opcion == 1:
            print("Resultado:", suma(a, b))
        elif opcion == 2:
            print("Resultado:", resta(a, b))
        elif opcion == 3:
            print("Resultado:", multiplicacion(a, b))
        elif opcion == 4:
            print("Resultado:", division(a, b))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()


--Aqui iran los fusiones con Merge

