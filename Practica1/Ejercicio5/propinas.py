def main():
    price = priceToFloat(input("Cual fue el precio de la cuenta? "))
    tipPercentage = tipPercentageToFloat(input("Que porcentaje de propina desea dar? "))
    tip = price * tipPercentage
    print(f"El total de la propina es: ${tip:.2f}")

def priceToFloat(price):
    priceRaw = price.replace("$", "").replace(",", "")
    priceRaw = float(priceRaw)
    return priceRaw


def tipPercentageToFloat(tipPercentage):
    tipPercentageRaw = tipPercentage.replace("%", "").replace(",", ".")
    tipPercentageRaw = float(tipPercentageRaw)
    return tipPercentageRaw / 100.0

if __name__ == "__main__":
    main()