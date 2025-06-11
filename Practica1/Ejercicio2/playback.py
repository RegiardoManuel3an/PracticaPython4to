def main():
    userInput = input("Ingrese una frase, palabra o sentencia: ")
    userCalm = str.replace(userInput, " ", "...")
    print("Su voz interior, calmadamente dice: " + userCalm)

if __name__ == "__main__":
    main()
