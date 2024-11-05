#Funcion Division Calculadora.py

def division(a, b):
    if b == 0:
        return "Error: División por cero."
    return a / b

def main():
    print("Calculadora de División:")
    print("4. División")

    opcion = int(input("Elige una operación (4 para División): "))

    # Solo permite continuar si se selecciona la opción 4
    if opcion == 4:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", division(a, b))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
