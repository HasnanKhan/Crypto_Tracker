import os
import requests
from dotenv import load_dotenv

load_dotenv()

COINDESK_API_KEY = os.getenv("COINDESK_API_KEY")
TEXTBELT_KEY = os.getenv("TEXTBELT_KEY")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

def xrp():
    url = f"https://data-api.coindesk.com/spot/v1/latest/tick?apply_mapping=true&market=coinbase&instruments=XRP-USD&groups=CURRENT_HOUR,VALUE&api_key={COINDESK_API_KEY}"
    return requests.get(url)

def btc():
    url = f"https://data-api.coindesk.com/spot/v1/latest/tick?apply_mapping=true&market=coinbase&instruments=BTC-USD&groups=CURRENT_HOUR,VALUE&api_key={COINDESK_API_KEY}"
    return requests.get(url)

def hbar():
    url = f"https://data-api.coindesk.com/spot/v1/latest/tick?apply_mapping=true&market=coinbase&instruments=HBAR-USD&groups=CURRENT_HOUR,VALUE&api_key={COINDESK_API_KEY}"
    return requests.get(url)

if __name__ == "__main__":
    x = xrp().json()
    b = btc().json()
    h = hbar().json()
    s = ""

    xrp_change = x['Data']['XRP-USD']['CURRENT_HOUR_CHANGE']
    btc_change = b['Data']['BTC-USD']['CURRENT_HOUR_CHANGE']
    hbar_change = h['Data']['HBAR-USD']['CURRENT_HOUR_CHANGE']

    if abs(xrp_change) > 0.01:
        s += 'XRP: ' + str(x['Data']['XRP-USD']['PRICE']) + " " + "Change: " + str(xrp_change) + '\n'
    if abs(btc_change) > 1000:
        s += 'BTC: ' + str(b['Data']['BTC-USD']['PRICE']) + " " + "Change: " + str(btc_change) + '\n'
    if abs(hbar_change) > 0.01:
        s += 'HBAR: ' + str(h['Data']['HBAR-USD']['PRICE']) + " " + "Change: " + str(hbar_change) + '\n'

    if s:
        requests.post('https://textbelt.com/text', {
            'phone': PHONE_NUMBER,
            'message': s,
            'key': TEXTBELT_KEY,
        })
