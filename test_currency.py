import requests

API_KEY = '9243071f5d31a162f57ddff6' # Replace with your actual API key
base_currency = 'AUD'
target_currency = 'CNY'

url = f'https://open.er-api.com/v6/latest/{base_currency}'
params = {
    'apikey': API_KEY
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    if target_currency in data['rates']:
        exchange_rate = data['rates'][target_currency]
        print(f"Current exchange rate from {base_currency} to {target_currency}: {exchange_rate}")
    else:
        print(f"Exchange rate for {target_currency} not found.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
