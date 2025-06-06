import requests


url = "https://api.monobank.ua/bank/currency"


response = requests.get(url)


if response.status_code == 200:
    data = response.json()

  
    for item in data:
        if item.get("currencyCodeA") == 840 and item.get("currencyCodeB") == 980:
            print("Exchange USD in UAH:")
            print("Buy:", item.get("rateBuy"))
            print("Sell:", item.get("rateSell"))
            break
else:
    print("Error:", response.status_code)