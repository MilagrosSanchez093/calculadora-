def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir entre cero."

def main():
    print("Bienvenido a la calculadora básica")

    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            operacion = input("Ingrese la operación (+, -, *, /): ")

            if operacion == '+':
                resultado = suma(num1, num2)
            elif operacion == '-':
                resultado = resta(num1, num2)
            elif operacion == '*':
                resultado = multiplicacion(num1, num2)
            elif operacion == '/':
                resultado = division(num1, num2)
            else:
                print("Operación no válida.")
                continue

            print("El resultado de la operación es:", resultado)
        except ValueError:
            print("Por favor, ingrese números válidos.")

        continuar = input("¿Desea realizar otra operación? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
