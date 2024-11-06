# Comandos usados, Fusiones creadas y Conflictos resueltos
Uso de comandos

#Creacion de calculadora.py

git add calculadora.py
git commit -m "calculadora main"

#Creacion de rama Develop
git checkout -b Develop
-Agrego un archivo de txt que se muestre que se esta en la rama Develop
git add develop.txt
git commit -m "rama DEVELOP"
-Se envia a la nube
git push --set-upstream origin Develop

#Creacion rama suma-feature (sin GitFlow)
git checkout -b suma-feature
-Agrego un archivo de txt que se muestre que se esta en la rama suma-feature
git add suma-feature.txt
git commit -m "descrip suma-feature"
git push --set-upstream origin suma-feature


#Creacion rama resta-feature
git checkout -b resta-feature
-Agrego un archivo de txt que se muestre que se esta en la rama resta-feature
git add resta-feature.txt
git commit -m "descrip txt resta"
git push --set-upstream origin resta-feature


#Creacion rama multiplicaicon-feature
git checkout -b multiplicacion-feature
-Agrego un archivo de txt que se muestre que se esta en la rama resta-feature
git add multiplicacion-feature.txt
git commit -m "multiplicacion txt"
git push --set-upstream origin multiplicacion-feature

#Creacion rama division-feature
git checkout -b division-feature
-Agrego un archivo de txt que se muestre que se esta en la rama resta-feature
git add division-feature.txt
git commit -m division-txt"
git push --set-upstream origin division-feature

#Creacion de calculadora.py para cada branch
suma-feature

##Funcion Suma Calculadora.py
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

##Funcion Resta Calculadora.py
# calculadoraResta.py

def resta(a, b):
    return a - b

def main():
    print("Calculadora de Resta:")
    print("2. Resta")

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

##Funcion Multiplicacion Calculadora.py
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

##Funcion Division
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

#Fusion en el Develop
#1 Fusionando suma-feature
git checkout Develop
git merge suma-feature
git add calculadora.py
git commit -m "Combinar funciones de suma y resta en calculadora.py"
git push origin Develop


#2 Fusionando resta-feature
git checkout develop
git merge resta-feature
git add calculadora.py
git commit -m "calculadoraSuma.py"
git push origin Develop

#3 Fusionando multiplicacion-feature
git merge multiplicacion-feature
git add calculadora.py
git commit -m "Combinar funciones de suma, resta y multiplicación en calculadora.py"
git push origin Develop

#4 Fusionando division-feature
git merge division-feature
git add calculadora.py
git commit -m "Integrar las funciones de suma, resta, multiplicación y división en calculadora.py"
git push origin Develop


###Fusionando Develop con Main
git checkout main
git merge develop
git add calculadora.py
git commit -m "Fusionar código completo y estable de calculadora desde develop a main"
git push origin main




1. Conflicto al querer hacer merge entre suma-feature y Develop
C:\Users\marce\Documents\GitTou\gitfinal\git_calculadora_avp>git merge suma-feature
error: Merging is not possible because you have unmerged files.
hint: Fix them up in the work tree, and then use 'git add/rm <file>'
hint: as appropriate to mark resolution and make a commit.
fatal: Exiting because of an unresolved conflict.


al darle al git status arroja esto:
Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   calculadora.py

entramos a nano calculadora.py
# calculadoraSuma.py

<<<<<<< HEAD


=======
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

eliminamos los <<< y los =====

pasa a verse asi:
def suma(a, b):
    return a + b

def main():
    print("Calculadora de Suma:")
    print("1. Suma")

    opcion = int(input("Elige una operación (1 para Suma): "))

    if opcion == 1:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", suma(a, b))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()

luego:
git add calculadora.py
git commit -m "Resolviendo 1 conflicto de fusion y agregar funcion suma"


2. Conflicto al querer hacer merge entre Develop (con Suma-Feature) y resta-feature
$ git merge resta-feature
Auto-merging calculadora.py
CONFLICT (content): Merge conflict in calculadora.py
Automatic merge failed; fix conflicts and then commit the result.

entramos a nano calculadora.py
se ve asi:
<<<<<<< HEAD
# calculadoraSuma.py

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
=======
# calculadoraResta.py

def resta(a, b):
    return a - b

def main():
    print("Calculadora de Resta:")
    print("2. Resta")

    opcion = int(input("Elige una operación (2 para Resta): "))

    # Solo permite continuar si se selecciona la opción 1
    if opcion == 2:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", resta(a, b))
>>>>>>> resta-feature
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()


esto ocasiona conflictos asi que lo modificaremos de la sgte manera:
  GNU nano 8.0                     calculadora.py                     Modified

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

luego:
git add calculadora.py
git commit -m "Combinando funciones de suma y resta"
git push origin Develop


3. Conflicto al querer hacer merge entre Develop (con Suma y Resta) y multiplicacion-feature
$ git merge multiplicacion-feature
Auto-merging calculadora.py
CONFLICT (content): Merge conflict in calculadora.py
Automatic merge failed; fix conflicts and then commit the result.

git status:
Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   calculadora.py

entramos a nano calculadora.py a arreglarlo 
<<<<<<< HEAD

# calculadora.py
=======
# calculadoraMultiplicacion.py
>>>>>>> multiplicacion-feature

def multiplicacion(a, b):
    return a * b

def resta(a, b):
    return a - b

def main():
<<<<<<< HEAD
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
=======
    print("Calculadora de Multiplicación:")
    print("3. Multiplicación")

    opcion = int(input("Elige una operación (3 para Multiplicación): "))

    # Solo permite continuar si se selecciona la opción 3
    if opcion == 3:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", multiplicacion(a, b))
>>>>>>> multiplicacion-feature
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()

se arregla para que las 3 funciones coexistan quedando asi:
# calculadora.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def main():
    print("Calculadora:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")

    opcion = int(input("Elige una operación (1 para Suma, 2 para Resta, 3 para Multiplicación): "))

    if opcion == 1:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la suma:", suma(a, b))
    elif opcion == 2:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la resta:", resta(a, b))
    elif opcion == 3:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la multiplicación:", multiplicacion(a, b))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main() 

luego 
git add calculadora.py
git commit -m "Combinar funciones de suma, resta y multiplicación en calculadora.py"
git push origin Develop


4. Conflicto al querer hacer merge entre Develop (suma, resto, multiplicacion) con division-feature
al hacer git status tenemos el siguiente conflicto:

$ git merge division-feature
Auto-merging calculadora.py
CONFLICT (content): Merge conflict in calculadora.py
Automatic merge failed; fix conflicts and then commit the result.

entramos a nano calculadora.py y tenemos lo siguiente
<<<<<<< HEAD
# calculadora.py

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b
=======
#Funcion Division Calculadora.py
>>>>>>> division-feature

def division(a, b):
    if b == 0:
        return "Error: División por cero."
    return a / b

def main():
<<<<<<< HEAD
    print("Calculadora:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")

    opcion = int(input("Elige una operación (1 para Suma, 2 para Resta, 3 para Multiplicación>

    if opcion == 1:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la suma:", suma(a, b))
    elif opcion == 2:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la resta:", resta(a, b))
    elif opcion == 3:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la multiplicación:", multiplicacion(a, b))
=======
    print("Calculadora de División:")
    print("4. División")

    opcion = int(input("Elige una operación (4 para División): "))

    # Solo permite continuar si se selecciona la opción 4
    if opcion == 4:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado:", division(a, b))
>>>>>>> division-feature
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()

lo cambiamos a:
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
    print("Calculadora:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = int(input("Elige una operación (1 para Suma, 2 para Resta, 3 para Multiplicación, 4 para División): "))

    if opcion == 1:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la suma:", suma(a, b))
    elif opcion == 2:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la resta:", resta(a, b))
    elif opcion == 3:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la multiplicación:", multiplicacion(a, b))
    elif opcion == 4:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la división:", division(a, b))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()

luego:
git add calculadora.py
git commit -m "Integrar las funciones de suma, resta, multiplicación y división en calculadora.py"
git push origin Develop

5. Conflicto al querer hacer merge entre Develop (Ver Estable) y main
$ git merge Develop
Auto-merging calculadora.py
CONFLICT (content): Merge conflict in calculadora.py
Automatic merge failed; fix conflicts and then commit the result.

entramos a nano calculadora.py para ver como se ve
# calculadora.py
#Aqui va el codigo estable una vez ya fusionado con Develop

<<<<<<< HEAD
=======
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
    print("Calculadora:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = int(input("Elige una operación (1 para Suma, 2 para Resta, 3 para Multiplicación>

    if opcion == 1:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la suma:", suma(a, b))
    elif opcion == 2:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la resta:", resta(a, b))
    elif opcion == 3:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la multiplicación:", multiplicacion(a, b))
    elif opcion == 4:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la división:", division(a, b))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()

>>>>>>> Develop

Se cambia a
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
    print("Calculadora:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = int(input("Elige una operación (1 para Suma, 2 para Resta, 3 para Multiplicación, 4 para División): "))

    if opcion == 1:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la suma:", suma(a, b))
    elif opcion == 2:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la resta:", resta(a, b))
    elif opcion == 3:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la multiplicación:", multiplicacion(a, b))
    elif opcion == 4:
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Resultado de la división:", division(a, b))
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()
luego 
git add calculadora.py
git commit -m "Fusionar código completo y estable de calculadora desde develop a main"
git push origin main
