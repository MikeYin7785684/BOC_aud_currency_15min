import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
 
def fetch_exchange_rates():
    url = 'https://www.boc.cn/sourcedb/whpj/'
    response = requests.get(url)
    response.encoding='utf-8'
    html_content = response.text
    soup=BeautifulSoup(html_content,'html.parser')
    currency=soup.find('td',string='澳大利亚元')
    currency_au_now=currency.find_parent('tr').contents[7].get_text()
    return float(currency_au_now)

    

if __name__ == "__main__":
    previous_rate = fetch_exchange_rates()
    
    while True:
        try:
            print(f"\n{datetime.now()}Fetching currency exchange rates...")
            current_rate = fetch_exchange_rates()
            
            if previous_rate!=current_rate:
                print("Changes detected:")
                print(f"aud: {previous_rate} -> {current_rate}")
            else:
                print("No changes detected.")
            previous_rate = current_rate
            time.sleep(900)  # Sleep for 15 minutes (900 seconds)
            
        except Exception as e:
            print(f"An error occurred: {e}")

