def calculoEnergia(masa):
    c = 299792458
    energia = masa * c ** 2
    return energia

def main():
    userInput = input("Ingrese la masa en Kilogramos: ")
    masa = int(userInput)
    if masa < 0:
        print("La masa no puede ser negativa.")
    else:
        energia = calculoEnergia(masa)
        print(f"La energía equivalente a {masa} kg es: {energia} Joules")

if __name__ == "__main__":
    main()