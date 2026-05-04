import requests

API_KEY = "4fba59670e538d3669fa7b33"

def get_rate(from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    return data["conversion_rates"][to_currency]