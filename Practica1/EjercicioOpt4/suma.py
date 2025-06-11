def main():
    userInput = input("Ingrese un numero: ")
    userInput2 = input("Ingrese otro numero: ")
    if not userInput.isdigit() or not userInput2.isdigit():
        print("Por favor, ingrese solo números enteros.")
        return
    suma = int(userInput) + int(userInput2)
    print("La suma de " + userInput + " y " + userInput2 + " es: " + str(suma))

if __name__ == "__main__":
    main()