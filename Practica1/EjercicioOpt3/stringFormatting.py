def main():
    userInput = input("Digite una frase, palabra o sentencia: ")
    lowerInput = userInput.lower()
    upperInput = userInput.upper()
    strippedInput = userInput.strip()
    print("String original: " + userInput)
    print("String en minúsculas: " + lowerInput)
    print("String en mayúsculas: " + upperInput)
    print("String sin espacios al inicio y al final: " + strippedInput)

if __name__ == "__main__":
    main()