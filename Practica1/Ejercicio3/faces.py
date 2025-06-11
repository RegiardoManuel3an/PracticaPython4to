def convert(userInput):
    r = userInput.replace(":)", "🙂").replace(":(", "🙁")
    return r

def main():
    userInput = input("Ingrese una frase, palabra o sentencia: ")
    emojifiedInput = convert(userInput)
    print("Su frase emojificada es: " + emojifiedInput)

if __name__ == "__main__":
    main()