import requests

class CurrencyConverter:
    """
    A class for converting currency using exchange rates fetched from an API.
    """

    def __init__(self):
        self.api_endpoint = "https://api.exchangerate-api.com/v4/latest/"

    def fetch_exchange_rate(self, from_currency, to_currency):
        """
        Fetches the latest exchange rate for the specified currencies.

        Args:
            from_currency (str): The currency to convert from.
            to_currency (str): The currency to convert to.

        Returns:
            float: The exchage rate from 'from_currency' to 'to_currency'.
        """

        url = f"{self.api_endpoint}/{from_currency}"
        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code ==200:
                exchange_rate = data['rates'][to_currency]
                return exchange_rate
            else:
                print("Unalbel to fecth exchange rates")

        except requests.exceptions.RequestException as e:
            print("Error",e)

    def convert(self, amount, from_currency, to_currency):
        """
        Converts the specified amount from one currency to another.

        Args:
            amount (float): The amount to convert.
            from_currency (str): The currency to convert from.
            to_currency (str): The currency to convert to.

        Returns:
            float: The converted amount.
        """
        exchange_rate = self.fetch_exchange_rate(from_currency, to_currency)

        if exchange_rate:
            converted_amount = amount * exchange_rate
            return converted_amount

# User input
amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from: ")
to_currency = input("Enter the currency to convert to: ")

# Creating an instance of the CurrencyConverter class
converter = CurrencyConverter()

# Calling the convert method
result = converter.convert(amount, from_currency, to_currency)

# Displaying the result
if result:
    print(f"{amount} {from_currency} is equal to {result} {to_currency}.")



"""
OUTPUT:
Enter the amount to convert: 1
Enter the currency to convert from: USD
Enter the currency to convert to: INR
1.0 USD is equal to 82.15 INR.
"""