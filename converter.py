# simple code to convert one currency to another from command line

from forex_python.converter import CurrencyRates

# Input amount
while True:
    try:
        amount = int(input("Enter amount of currency you want to exchange: "))
        break
    except ValueError:
        print("Please enter an integer.")
# Input type of conversion
src_currency = input("Enter currency code to convert from(ex. USD): ")
dest_currency = input("Enter currency code to conver to(ex. EUR): ")
# create an instance of CurrencyRates
cr = CurrencyRates()

# Convert
result = cr.convert(src_currency, dest_currency, amount)
print(f"{amount} {src_currency} is equal to {result} {dest_currency}")
