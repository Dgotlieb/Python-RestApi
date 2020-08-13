import requests
res = requests.get('https://free.currencyconverterapi.com/api/v6/convert?q=USD_ILS&compact=n&apiKey=XXXXXX') # change key
if res.ok:
    results = res.json()['results']
    USD_ILS = results['USD_ILS']
    val = USD_ILS['val']
    print(val)
