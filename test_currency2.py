import requests
from bs4 import BeautifulSoup
import time
 
def fetch_exchange_rates():
    url = 'https://www.boc.cn/sourcedb/whpj/'
    response = requests.get(url)
    response.encoding='utf-8'
    html_content = response.text
    soup=BeautifulSoup(html_content,'html.parser')
    currency=soup.find('td',string='澳大利亚元')
    currency_au_now=currency.find_parent('tr').contents[7]
    return currency_au_now

# Function to detect currency changes
def detect_currency_changes(previous_rates, current_rates):
    changes = {}
    for currency, rate in current_rates.items():
        if currency in previous_rates:
            if rate != previous_rates[currency]:
                changes[currency] = (previous_rates[currency], rate)
    return changes

if __name__ == "__main__":
    previous_rates = fetch_exchange_rates()
    
    while True:
        try:
            print("\nFetching currency exchange rates...")
            current_rates = fetch_exchange_rates()
            changes = detect_currency_changes(previous_rates, current_rates)
            
            if changes:
                print("Changes detected:")
                for currency, (previous_rate, current_rate) in changes.items():
                    print(f"{currency}: {previous_rate} -> {current_rate}")
            else:
                print("No changes detected.")
                
            previous_rates = current_rates
            time.sleep(900)  # Sleep for 15 minutes (900 seconds)
            
        except Exception as e:
            print(f"An error occurred: {e}")

